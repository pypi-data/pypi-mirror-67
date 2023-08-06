from threading import Event
import logging
from typing import Union
import typing

from pyobs.comm import Comm
from pyobs.interfaces import ITelescope, ICamera, IFilters, IRoof, IAutoGuiding
from pyobs.robotic.lco.default import LcoDefaultScript
from pyobs.robotic.scripts import Script
from pyobs.robotic.task import Task
from pyobs.utils.time import Time

log = logging.getLogger(__name__)


class ConfigStatus:
    """Status of a single configuration."""

    def __init__(self, state='ATTEMPTED', reason=''):
        """Initializes a new Status with an ATTEMPTED."""
        self.start = Time.now()
        self.end = None
        self.state = state
        self.reason = reason
        self.time_completed = 0

    def finish(self, state=None, reason=None, time_completed: int = 0) -> 'ConfigStatus':
        """Finish this status with the given values and the current time.

        Args:
            state: State of configuration
            reason: Reason for that state
            time_completed: Completed time [s]
        """
        if state is not None:
            self.state = state
        if reason is not None:
            self.reason = reason
        self.time_completed = time_completed
        self.end = Time.now()
        return self

    def to_json(self):
        """Convert status to JSON for sending to portal."""
        return {
            'state': self.state,
            'summary': {
                'state': self.state,
                'reason': self.reason,
                'start': self.start.isot,
                'end': self.end.isot,
                'time_completed': self.time_completed
            }
        }


class LcoTask(Task):
    """A task from the LCO portal."""

    def __init__(self, config: dict, comm: Comm, telescope: str, camera: str, filters: str, roof: str,
                 autoguider: str, scripts: typing.Dict[str, Script], *args, **kwargs):
        """Init LCO task (called request there).

        Args:
            config: Configuration for task
            comm: Comm object to use
            telescope: Telescope to use
            camera: Camera to use
            filters: Filters to use
            roof: Roof to use
            autoguider: Autoguider to use
            scripts: External scripts to run
        """
        Task.__init__(self, *args, **kwargs)

        # store stuff
        self.config = config
        self.comm = comm
        self.telescope = telescope
        self.camera = camera
        self.filters = filters
        self.roof = roof
        self.autoguider = autoguider
        self.scripts = scripts
        self.cur_script = None

    @property
    def id(self) -> str:
        """ID of task."""
        return self.config['request']['id']

    @property
    def name(self) -> str:
        """Returns name of task."""
        return self.config['name']

    @property
    def duration(self) -> float:
        """Returns estimated duration of task in seconds."""
        return self.config['request']['duration']

    def window(self) -> (Time, Time):
        """Returns the time window for this task.

        Returns:
            Start and end time for this observation window.
        """
        return self.config['start'], self.config['end']

    def _get_proxies(self) -> (IRoof, ITelescope, ICamera, IFilters):
        """Get proxies for running the task

        Returns:
            Proxies for roof, telescope, camera and filter wheel

        Raises:
            ValueError: If could not get proxies for all modules
        """
        roof: IRoof = self.comm.proxy(self.roof, IRoof)
        telescope: ITelescope = self.comm.proxy(self.telescope, ITelescope)
        camera: ICamera = self.comm.proxy(self.camera, ICamera)
        filters: IFilters = self.comm.proxy(self.filters, IFilters)
        autoguider: IAutoGuiding = self.comm.proxy(self.autoguider, IAutoGuiding)
        return roof, telescope, camera, filters, autoguider

    def _get_config_script(self, config: dict, roof: IRoof, telescope: ITelescope, camera: ICamera,
                           filters: IFilters, autoguider: IAutoGuiding) -> Script:
        """Get config script for given configuration.

        Args:
            config: Config to create runner for.
            roof: Roof
            telescope: Telescope
            camera: Camera
            filters: Filter wheel
            autoguider: Auto guider

        Returns:
            Script for running config

        Raises:
            ValueError: If could not create runner.
        """

        # what do we run?
        if 'extra_params' in config and 'script_name' in config['extra_params']:
            # let's run some script, so get its name
            script_name = config['extra_params']['script_name']

            # got one?
            if script_name in self.scripts:
                return self.scripts[script_name]
            else:
                raise ValueError('Invalid script task type.')

        else:
            # seems to be a default task
            from .taskarchive import LcoTaskArchive
            self.task_archive: LcoTaskArchive
            return LcoDefaultScript(config, roof, telescope, camera, filters, autoguider, self.task_archive.instruments)

    def can_run(self) -> bool:
        """Checks, whether this task could run now.

        Returns:
            True, if task can run now.
        """

        # get proxies
        try:
            roof, telescope, camera, filters, autoguider = self._get_proxies()
        except ValueError:
            return False

        # loop configurations
        req = self.config['request']
        for config in req['configurations']:
            # get config runner
            runner = self._get_config_script(config, roof, telescope, camera, filters, autoguider)

            # if any runner can run, we proceed
            if runner.can_run():
                return True

        # no config found that could run
        return False

    def run(self, abort_event: Event):
        """Run a task

        Args:
            abort_event: Event to be triggered to abort task.
        """
        from pyobs.robotic.lco import LcoTaskArchive

        # get request
        req = self.config['request']

        # get proxies
        try:
            roof, telescope, camera, filters, autoguider = self._get_proxies()
        except ValueError:
            # fail all configs
            log.error('Could not get proxies.')
            for config in req['configurations']:
                # send status
                status = ConfigStatus()
                if isinstance(self.task_archive, LcoTaskArchive):
                    self.config['state'] = 'FAILED'
                    self.task_archive.send_update(config['configuration_status'],
                                                  status.finish(state='FAILED', reason='System failure.').to_json())

            # finish
            return

        # loop configurations
        for config in req['configurations']:
            # aborted?
            if abort_event.is_set():
                break

            # send an ATTEMPTED status
            if isinstance(self.task_archive, LcoTaskArchive):
                status = ConfigStatus()
                self.config['state'] = 'ATTEMPTED'
                self.task_archive.send_update(config['configuration_status'], status.finish().to_json())

            # get config runner
            script = self._get_config_script(config, roof, telescope, camera, filters, autoguider)

            # can run?
            if not script.can_run():
                log.warning('Cannot run config.')
                continue

            # run config
            log.info('Running config...')
            self.cur_script = script
            status = self._run_script(abort_event, script)
            self.cur_script = None

            # send status
            if status is not None and isinstance(self.task_archive, LcoTaskArchive):
                self.config['state'] = status.state
                self.task_archive.send_update(config['configuration_status'], status.to_json())

        # finished task
        log.info('Finished task.')

    def _run_script(self, abort_event, script: Script) -> Union[ConfigStatus, None]:
        """Run a config

        Args:
            abort_event: Event for signaling abort
            script: Script to run

        Returns:
            Configuration status to send to portal
        """

        # at least we tried...
        config_status = ConfigStatus()

        try:
            # check first
            self._check_abort(abort_event)

            # run it
            log.info('Running task %d: %s...', self.id, self.config['name'])
            script.run(abort_event)

            # finished config
            config_status.finish(state='COMPLETED', time_completed=script.exptime_done)

        except InterruptedError:
            log.warning('Task execution was interrupted.')
            config_status.finish(state='FAILED', reason='Task execution was interrupted.',
                                 time_completed=script.exptime_done)

        except Exception:
            log.exception('Something went wrong.')
            config_status.finish(state='FAILED', reason='Something went wrong', time_completed=script.exptime_done)

        # finished
        return config_status

    def is_finished(self) -> bool:
        """Whether task is finished."""
        return self.config['state'] != 'PENDING'

    def get_fits_headers(self, namespaces: list = None) -> dict:
        """Returns FITS header for the current status of this module.

        Args:
            namespaces: If given, only return FITS headers for the given namespaces.

        Returns:
            Dictionary containing FITS headers.
        """

        # get header from script
        hdr = self.cur_script.get_fits_headers(namespaces) if self.cur_script is not None else {}

        # return it
        return hdr


__all__ = ['LcoTask']
