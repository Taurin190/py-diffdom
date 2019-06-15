# -*- coding:utf-8 -*-
from config import config_manager as cm


class DBConfig(object):
    def __init__(self, hostname, port, type, database, collection):
        self.hostname = hostname
        self.port = port
        self.type = type
        self.database = database
        self.collection = collection


class DBConfigManager(cm.ConfigManager):
    def __init__(self, file_path):
        super().__init__(file_path)

    def get_config_obj(self):
        hostname = self.config["database"]["hostname"]
        port = self.config["database"]["port"]
        type = self.config["database"]["database"]
        database = self.config["database"]["database"]
        collection = self.config["database"]["collection"]
        return DBConfig(hostname, port, type, database, collection)

