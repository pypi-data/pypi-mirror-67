# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function
from zabbix_sys.tools.logger import get_logger
import os
import yaml
import platform


CONFIGS = {
    'linux': [
        os.path.abspath(os.path.expanduser("~/.zabbix/config.yml")),
        os.path.abspath(os.path.expanduser("~/.zabbix/im.sys.conf.yml")),
        os.path.abspath("/var/lib/zabbix/config.yml"),
        os.path.abspath("/var/lib/zabbix/im.sys.conf.yml"),
        os.path.abspath("/etc/zabbix/config.yml"),
        os.path.abspath("/etc/zabbix/im.sys.conf.yml")
    ],
    'darwin': [
        os.path.abspath(os.path.expanduser("~/.zabbix/config.yml")),
        os.path.abspath(os.path.expanduser("~/.zabbix/im.sys.conf.yml")),
        os.path.abspath("/var/lib/zabbix/config.yml"),
        os.path.abspath("/var/lib/zabbix/im.sys.conf.yml"),
        os.path.abspath("/etc/zabbix/config.yml"),
        os.path.abspath("/etc/zabbix/im.sys.conf.yml")
    ],
    'windows': [
        os.path.abspath(os.path.expanduser("~\\.zabbix\\config.yml")),
        os.path.abspath(os.path.expanduser("~\\.zabbix\\im.sys.conf.yml")),
        os.path.abspath("C:\\ProgramData\\Tools\\Zabbix\\config.yml"),
        os.path.abspath("C:\\ProgramData\\Tools\\Zabbix\\im.sys.conf.yml")
    ]
}


def get_platform():

    system = str(platform.system()).lower()
    if system in CONFIGS.keys():
        return system
    else:
        return None


def get_config():

    system = get_platform()
    logger = get_logger()
    config = None

    if system:
        for f in CONFIGS[system]:
            if os.path.isfile(f):
                try:
                    with open(f) as stream:
                        config = yaml.safe_load(stream)
                    break
                except yaml.MarkedYAMLError as err:
                    logger.critical(msg="Error when parse yaml config " + str(err.context_mark).strip(), exc_info=False)
                    raise
    return config
