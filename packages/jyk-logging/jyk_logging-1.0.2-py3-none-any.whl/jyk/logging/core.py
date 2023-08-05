import os
import time
import json
import copy
import threading
import logging
import logging.handlers
from pathlib import Path

from .colors import red, yellow, cyan
from .formatter import JsonFormatter

log = logging.getLogger(__name__)

_tasks = {}
_loggers = {}

LOG_ROOT = os.getcwd()


class FormatterMode(object):
    BRIEF = "brief"
    INTACT = 'intact'


class Singleton(type):
    """Singleton.
    @see: http://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,
                                        cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class LogRootPath(metaclass=Singleton):
    """set jyk logging Root
    Args:
        log_root: `PathLike` Log Root Path
    """
    _root = None

    @classmethod
    def set(self, log_root):
        self._root = log_root

    @classmethod
    def get(self):
        if self._root is None:
            self._root = LOG_ROOT

        return self._root


def getLogPath(*args, **kwargs):
    """
    Returns:
        absolute path of file named name in the jyk log directory
    """
    _ROOT = Path(LogRootPath.get())

    if kwargs.get("root"):
        return _ROOT
    else:
        return _ROOT.joinpath(*args)


class DatabaseHandler(logging.Handler):
    """Logging to database"""
    def emit(self, recored):
        raise NotImplementedError


class TaskHandler(logging.Handler):
    """Per-task logger.
    Used to log all task specific events to a per-task jyk.log log file.
    """
    def emit(self, record):
        task_id = _tasks.get(threading.get_ident())
        if not task_id:
            return

        with open(getLogPath("jyk.log", analysis=task_id), "a+b") as f:
            f.write("%s\n" % self.format(record))


class ConsoleHandler(logging.StreamHandler):
    """Logging to console handler"""
    def emit(self, record):
        colored = copy.copy(record)

        if record.levelname == "WARNING":
            colored.msg = yellow(record.msg)
        elif record.levelname == "ERROR" or record.levelname == "CRITICAL":
            colored.msg = red(record.msg)
        else:
            if "analysis completed" in record.msg:
                colored.msg = cyan(record.msg)
            else:
                colored.msg = record.msg

        logging.StreamHandler.emit(self, colored)


def taskLogStart(task_id):
    """Associate a threading with a task."""
    _tasks[threading.get_ident()] = task_id


def taskLogStop(task_id):
    """Disassociate a threading from a task."""
    _tasks.pop(threading.get_ident(), None)


def initLogger(name: str, level=None, mode=FormatterMode.INTACT) -> None:
    """init Logger
    Args:
        name: name
        level: logging.level
    """
    if mode == FormatterMode.INTACT:
        formatter = logging.Formatter(
            "%(asctime)s [%(name)s] %(levelname)s: %(message)s")
    else:
        formatter = logging.Formatter("[%(name)s]: %(message)s")

    if name == "console":
        log = ConsoleHandler()
        log.setFormatter(formatter)
        log.setLevel(level)

    if name == "database":
        log = DatabaseHandler()
        log.setLevel(logging.ERROR)

    if name == "task":
        log = TaskHandler()
        log.setFormatter(formatter)

    if name.endswith(".json"):
        j = JsonFormatter()
        log = logging.handlers.WatchedFileHandler(getLogPath(name), encoding='utf-8')
        log.setFormatter(j)

    if name.endswith(".log"):
        log = logging.handlers.WatchedFileHandler(getLogPath(name), encoding='utf-8')
        log.setFormatter(formatter)
        log.setLevel(level)

    _loggers[name] = log
    logging.getLogger().addHandler(log)


def logger(message, *args, **kwargs):
    """Log a message to specific logger instance."""
    logfile = kwargs.pop("logfile", None)
    record = logging.LogRecord(None, logging.INFO, None, None, message, args,
                               None, None)
    record.asctime = "%s,%03d" % (time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime(record.created)), record.msecs)
    record.message = record.getMessage()
    record.__dict__.update(kwargs)

    for key, value in _loggers.items():
        if logfile and key == logfile:
            value.handle(record)
        if logfile is None and key.endswith(".json"):
            value.handle(record)


def initConsoleLogging(level=logging.INFO, mode=FormatterMode.BRIEF):
    """Initializes logging only to console.
    Args:
        level: logging.level
    """
    logging.getLogger().setLevel(logging.DEBUG)
    initLogger("console", level, mode)


def initLogging(name, level=logging.INFO, mode=FormatterMode.INTACT):
    """Initializes logging.
    Args:
        level: logging.level
    """
    logging.getLogger().setLevel(logging.DEBUG)
    initLogger(name, level, mode)


__all__ = ["initConsoleLogging", "initLogging", "LogRootPath"]
