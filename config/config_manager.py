# -*- coding:utf-8 -*-
import configparser
import os
from abc import abstractmethod


class ConfigManager:
    def __init__(self, file_path):
        current_path = os.getcwd()
        self.config = configparser.ConfigParser()
        self.config.read(current_path + "/" + file_path)
        print("read config file with:" + current_path + file_path)

    @abstractmethod
    def get_config_obj(self):
        raise NotImplementedError()



