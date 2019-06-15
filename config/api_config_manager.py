# -*- coding:utf-8 -*-
from config import config_manager as cm


class APIConfig(object):
    def __init__(self, url1, port1, url2, port2, type):
        self.url1 = url1
        self.port1 = port1
        self.url2 = url2
        self.port2 = port2
        self.type = type


class APIConfigManager(cm.ConfigManager):
    def __init__(self, file_path):
        super().__init__(file_path)

    def get_config_obj(self):
        url1 = self.config["api"]["url1"]
        port1 = self.config["api"]["port1"]
        url2 = self.config["api"]["url2"]
        port2 = self.config["api"]["port2"]
        type = self.config["api"]["type"]
        return APIConfig(url1, port1, url2, port2, type)

