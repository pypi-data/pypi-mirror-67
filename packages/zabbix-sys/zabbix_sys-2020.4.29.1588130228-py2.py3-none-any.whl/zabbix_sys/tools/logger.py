# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function
import logging
import logging.handlers
import json
import os
import platform
import yaml


LOG_LEVELS = {
    'critical': logging.CRITICAL,
    'fatal': logging.CRITICAL,
    'error': logging.ERROR,
    'warning': logging.WARNING,
    'warn': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG,
    'notset': logging.NOTSET
}


# TODO: Add syslog and maybe gelf handlers
# TODO: Json formatter fix problems with quotas
# TODO: Refactoring get_logger code
def get_logger(config=None):

    if not config or not isinstance(config, dict):
        config = {}

    logger = logging.getLogger(name='__main__')

    for handler in logger.handlers:
        logger.removeHandler(handler)

    handlers = config.get('logs', [])

    if not handlers or not isinstance(handlers, list):
        logger_handler = logging.StreamHandler()
        logger_handler.setLevel(logging.ERROR)
        logger_handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(message)s'))
        logger.addHandler(logger_handler)
        return logger

    for handler in handlers:
        if not isinstance(handler, dict) or not handler.get('enabled', True) or not handler.get('type', False):
            continue

        logger_level = LOG_LEVELS.get(str(handler.get('level', 'error')).lower(), logging.ERROR)
        if logger.level == 0 or logger_level < logger.level:
            logger.setLevel(logger_level)

        logger_type = str(handler.get('type')).lower()
        logger_format = str(handler.get('format', 'text')).lower()

        logger_formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

        if logger_format == 'json':
            logger_formatter = logging.Formatter(
                "{\"time\":\"%(asctime)s\", \"level\": \"%(levelname)s\", \"message\": \"%(message)s\"}"
            )

        if logger_type == 'console':
            logger_handler = logging.StreamHandler()
            logger_handler.setLevel(logger_level)
            logger_handler.setFormatter(logger_formatter)
            logger.addHandler(logger_handler)

        if logger_type == 'file':
            logger_file = handler.get('file', None)
            if logger_file:
                filename = os.path.abspath(os.path.expanduser(logger_file))

                if os.path.isdir(os.path.dirname(filename)):
                    logger_handler = logging.handlers.RotatingFileHandler(
                        filename=filename, mode='a', maxBytes=10*1024*1024, backupCount=5
                    )

                    logger_handler.setLevel(logger_level)
                    logger_handler.setFormatter(logger_formatter)
                    logger.addHandler(logger_handler)

    return logger
