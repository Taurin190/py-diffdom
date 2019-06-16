# -*- coding:utf-8 -*-
from config.config_manager import ConfigManager


class AppConfig(object):
    def __init__(self, type, target1, target2):
        self.type = type
        self.target1 = target1
        self.target2 = target2


class AppConfigManager(ConfigManager):
    def __init__(self, file_path):
        super().__init__(file_path)

    def get_config_obj(self):
        type = self.config["app"]["type"]
        target1 = self.config["app"]["target1"]
        target2 = self.config["app"]["target2"]
        return AppConfig(type, target1, target2)
