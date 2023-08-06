import logging
import os
import sys

from .info import __version__, __sha1__

LOGGING_CONFIG = dict(
    version=1,
    disable_existing_loggers=False,

    loggers={
        # Route all non-sanic root logs via console
        "": {
            "level": logging.INFO,
            "handlers": ["console"],
            "propagate": False,
        },
        "sanic.root": {
            "level": logging.INFO,
            "handlers": ["console"],
            "propagate": False,
        },
        "sanic.error": {
            "level": logging.ERROR,
            "handlers": ["error_console"],
            "propagate": False,
            "qualname": "sanic.error"
        },
        "sanic.access": {
            "level": logging.INFO,
            "handlers": ["access_console"],
            "propagate": False,
            "qualname": "sanic.access"
        }
    },
    handlers={
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "json",
            "stream": sys.stdout
        },
        "error_console": {
            "class": "logging.StreamHandler",
            "formatter": "json",
            "level": logging.ERROR,
            "stream": sys.stderr
        },
        "access_console": {
            "class": "logging.StreamHandler",
            "formatter": "json",
            "stream": sys.stdout
        },
    },
    formatters={
        "generic": {
            "format": "%(asctime)s [%(process)d] [%(levelname)s] %(message)s",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter"
        },
        "json": {
            "class": "jsonlogging.JSONFormatter"
        },
        "access": {
            "format": "%(asctime)s - (%(name)s)[%(levelname)s][%(host)s]: " +
                      "%(request)s %(message)s %(status)d %(byte)d",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter"
        },
    }
)

ENVIRONMENT = os.getenv('ENVIRONMENT', 'development').lower()
DEBUG = bool(os.getenv('DEBUG', '').strip())

default_configuration = {
    'ENVIRONMENT': ENVIRONMENT,
    'DEBUG': DEBUG,
}


class AppConfiguration:
    VERSION = __version__
    SHA1 = __sha1__
