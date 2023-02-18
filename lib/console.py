"""
Console interactions are handled here.
"""
import inspect
import os
from datetime import datetime


class BasicFormatter:
    # availableKwargs = ["level", "levelname", "message", "asctime", "file", "filename"]

    def __init__(self, fmt: str = "%(levelname)s: %(message)s", datefmt: str = "%H:%M:%S"):
        self.fmt = fmt
        self.datefmt = datefmt

    def setFormat(self, fmt, datefmt=None):
        self.fmt = fmt
        if datefmt is not None:
            self.datefmt = datefmt

    def format(self, logger: "Logger", message: str, level: int, *args, **kwargs):
        """Format full message, and return the printable result"""
        # Check if the fmt contains "levelName"
        if "%(levelname)" in self.fmt:
            kwargs["levelname"] = logger.getLevelName(level)
        if "%(level)" in self.fmt:
            kwargs["level"] = level
        if "%(asctime)" in self.fmt:
            kwargs["asctime"] = datetime.now().strftime(self.datefmt)
        if "%(file)" in self.fmt:
            kwargs["file"] = inspect.stack()[2].filename
        if "%(filename)" in self.fmt:
            kwargs["filename"] = os.path.basename(inspect.stack()[2].filename)

        completeMessage = message % args
        return self.fmt % {"message": completeMessage, **kwargs}


class Logger:
    """
    This class handles logging to the console.
    """

    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50
    INPUT = 100

    def __init__(self):
        self.__levelNames = {
            self.DEBUG: "DEBUG",
            self.INFO: "INFO",
            self.WARNING: "WARNING",
            self.ERROR: "ERROR",
            self.CRITICAL: "CRITICAL",
            self.INPUT: "INPUT",
        }
        self.level = self.INFO
        self.formatter = BasicFormatter()

    def setLevel(self, level: int | str):
        if isinstance(level, str):
            level = level.upper()
            if level == "DEBUG":
                self.level = self.DEBUG
            elif level == "INFO":
                self.level = self.INFO
            elif level == "WARNING":
                self.level = self.WARNING
            elif level == "ERROR":
                self.level = self.ERROR
            elif level == "CRITICAL":
                self.level = self.CRITICAL
            elif level == "INPUT":
                self.level = self.INPUT
            else:
                raise ValueError("Invalid log level")
        elif isinstance(level, int):
            self.level = level
        else:
            raise TypeError("Invalid log level")

    def setFormatter(self, formatter: BasicFormatter):
        self.formatter = formatter

    def log(self, level: int, message: str, *args, **kwargs):
        formatted = self.formatter.format(self, level, message, *args, **kwargs)
        print(formatted)

    def inputLog(self, level: int, message: str, *args, **kwargs):
        formatted = self.formatter.format(self, level, message, *args, **kwargs)
        return input_(formatted)

    def getLevelName(self, level: int):
        return self.__levelNames[level]

    def setLevelName(self, level: int, name: str):
        self.__levelNames[level] = name

    def getLevel(self):
        return self.level


logger = Logger()

DEBUG = logger.DEBUG
INFO = logger.INFO
WARNING = logger.WARNING
ERROR = logger.ERROR
CRITICAL = logger.CRITICAL
INPUT = logger.INPUT


def setLevel(level: int | str):
    """
    Set the log level.
    """
    logger.setLevel(level)


def getLevelName(level: int):
    """
    Get the name of a log level.
    """
    return logger.getLevelName(level)


def setLevelName(level: int, name: str):
    """
    Set the name of a log level.
    """
    logger.setLevelName(level, name)


def debug(message, *args):
    """
    Log a debug message to the console.
    """
    if logger.level <= logger.DEBUG:
        logger.log(message, logger.DEBUG, *args)


def info(message, *args):
    """
    Log an info message to the console.
    """
    if logger.level <= logger.INFO:
        logger.log(message, logger.INFO, *args)


def warning(message, *args):
    """
    Log a warning message to the console.
    """
    if logger.level <= logger.WARNING:
        logger.log(message, logger.WARNING, *args)


def error(message, *args):
    """
    Log an error message to the console.
    """
    if logger.level <= logger.ERROR:
        logger.log(message, logger.ERROR, *args)


def critical(message, *args):
    """
    Log a critical message to the console.
    """
    if logger.level <= logger.CRITICAL:
        logger.log(message, logger.CRITICAL, *args)


input_ = input


def input(message, *args):
    """
    Log an input message to the console.
    """
    if logger.level <= logger.INPUT:
        return logger.inputLog(message, logger.INPUT, *args)
    else:
        return None
