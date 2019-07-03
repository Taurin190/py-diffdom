# -*- coding:utf-8 -*-
from config.config_manager import ConfigManager


class AppConfig(object):
    def __init__(self, config):
        self.type = config["app"]["type"]
        self.target1 = config["app"]["target1"]
        self.target2 = config["app"]["target2"]


class AppConfigManager(ConfigManager):
    def __init__(self, file_path):
        super().__init__(file_path)

    def get_html_config(self):
        return ""

    def get_config_obj(self):
        return AppConfig(self.config)
