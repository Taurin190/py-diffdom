# -*- coding:utf-8 -*-
import configparser
from abc import abstractmethod


class ConfigManager:
    def __init__(self, file_path):
        current_path = os.getcwd()
        self.config = configparser.ConfigParser()
        self.config.read(current_path + file_path)

    @abstractmethod
    def get_config_obj(self):
        raise NotImplementedError()



