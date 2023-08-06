"""Main module."""
import sys
import json
import time
import logging

from . import helpers
from .defaults import ACL, DEFAULT_FORMAT


class centrallog(logging.getLoggerClass()):
    """centrallog(self, name)
    Custom Logger class which extends the functionality of the existing
    Logger. 'name' is the name of logger. Do not instantiate this class
    directly instead use getLogger() static method of the class.
    The 'acl' parameter in most of the function is Access Control List,
    which tells whether the log is for developer(1), support(2) or
    customer(4).

    -------------------------------------------------------------------
    Usage:
    from myoperator.centrallog import centrallog
    logger = centrallog.getLogger()
    logger.log('test.', acl=4)
    -------------------------------------------------------------------

    Additional methods defined:

    dlog(self, level, message, *args, **kwargs)
        Write developer logs.

    slog(self, level, message, *args, **kwargs)
        Write support logs.

    clog(self, level, message, *args, **kwargs)
        Write customer logs.
    """
    _SERVICENAME = None
    _HOSTNAME = helpers.get_host_IP()
    _UID = helpers.get_uuid()
    _INDENT = None

    def __init__(self, name):
        self._title = ''
        logging.Logger.__init__(self, name)

    @staticmethod
    def getLogger(name=None):
        if centrallog._SERVICENAME is None:
            # default configuration if not configured yet
            centrallog.configure(name or 'root', centrallog._HOSTNAME,
                                 centrallog._UID)
        return logging.getLogger(name)

    @staticmethod
    def configure(servicename: str, hostname='', uid='', indent=None):
        if isinstance(servicename, str):
            centrallog._SERVICENAME = servicename
            centrallog._HOSTNAME = hostname
            centrallog._UID = uid,
            centrallog._INDENT = indent
        else:
            raise ValueError("Service name must be a string.")

    @staticmethod
    def get_configuration():
        """Get the configurations set by configure() method"""
        return (centrallog._SERVICENAME, centrallog._HOSTNAME, centrallog._UID, centrallog._INDENT)

    @staticmethod
    def is_configured():
        """Check if configurations are already set."""
        return centrallog._SERVICENAME is not None

    def process(self, message, kwargs):
        """Format the message captured for every log.
        """
        acl = kwargs.pop('acl', ACL['developer'])
        acl_values = set(ACL.values())
        if acl not in acl_values:
            raise ValueError("Invalid acl value. Possible values are %s."
                             % list(acl_values))

        if 'title' in kwargs:
            # set title if given.
            self.title(kwargs.pop('title'))

        epoch = time.time()
        msg_body = {
            "time": int(epoch),
            "mc_time": epoch,
            "ip": centrallog._HOSTNAME,
            "service": centrallog._SERVICENAME,
            "class": self.name,
            "data": {
                "uid": centrallog._UID,
                "msg": message,
                "acl": acl
            },
            "title": self._title,
        }

        # check if exc_info if passed
        exc_info = kwargs.pop('exc_info', None)
        if exc_info:
            if isinstance(exc_info, BaseException):
                exc_info = (type(exc_info), exc_info, exc_info.__traceback__)
            elif not isinstance(exc_info, tuple):
                exc_info = sys.exc_info()

            tb_str = helpers.get_exception_traceback(exc_info)
            msg_body['data']['exception'] = {
                "type": exc_info[0].__name__ if exc_info[0] else exc_info[0],
                "message": str(exc_info[1]) if exc_info[1] else exc_info[1],
                "traceback": tb_str.replace('\n', ' | ')
            }

        return json.dumps(msg_body, indent=centrallog._INDENT, default=str), kwargs

    def dlog(self, level, message, *args, **kwargs):
        """
        Delegate the developer log to the underlying logger.
        """
        kwargs['acl'] = ACL['developer']
        self.log(level, message, *args, **kwargs)

    def slog(self, level, message, *args, **kwargs):
        """
        Delegate the support log to the underlying logger.
        """
        kwargs['acl'] = ACL['support']
        self.log(level, message, *args, **kwargs)

    def clog(self, level, message, *args, **kwargs):
        """
        Delegate the customer log to the underlying logger.
        """
        kwargs['acl'] = ACL['customer']
        self.log(level, message, *args, **kwargs)

    def _log(self, level, message, args, **kwargs):
        """All log dispatcher (overridden method).
        """
        message, kwargs = self.process(message, kwargs)
        super()._log(level, message, args, **kwargs)
        self.reset_title()

    def title(self, text=''):
        """Set title for the log message."""
        self._title = text
        return self

    def reset_title(self):
        """Reset title value."""
        self._title = ''


logging.setLoggerClass(centrallog)
logging.basicConfig(level=logging.INFO, format=DEFAULT_FORMAT)
