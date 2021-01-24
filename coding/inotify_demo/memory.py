import logging
import threading

from .inotify import INotify, flags


class InotifyTotalMemory(object):
    def __init__(self):
        self.manager = NodeSoftwareManager()
        self.hostname = self.manager.get_name()

        self._inotify = INotify()
        self._worker = None
        self._start()

    def _start(self):
        t = threading.Thread(target=self._run)
        t.daemon = True
        t.start()

        self._worker = t

    def _refresh_hostname(self):
        try:
            new_hostname = self.manager.get_name()
            logging.info("hostname changed: {} --> {}".format(self.hostname, new_hostname))
            self.hostname = new_hostname
        except Exception as e:
            logging.exception(e)

    def _run(self):
        # `man inotify`: IN_DELETE_SELF and IN_IGNORED event
        watch_flags = flags.DELETE_SELF | flags.IGNORED
        self._inotify.add_watch("/etc/hostname", watch_flags)

        while True:
            # block until first event coming and wait another 3s for following events
            for event in self._inotify.read(read_delay=3000):
                event_flags = [str(f) for f in flags.from_mask(event.mask)]
                logging.info("inotify: {} {}".format(
                    event, "|".join(event_flags)
                ))
                if event.mask & flags.DELETE_SELF:
                    self._refresh_hostname()
                if event.mask & flags.IGNORED:
                    logging.info("re-watch new /etc/hostname")
                    self._inotify.add_watch("/etc/hostname", watch_flags)


hostify = InotifyHostInfo()
