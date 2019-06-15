# -*- coding:utf-8 -*-


class APIConfigManager(ConfigManager):
    def __init__(self, file_path):
        super(DBConfigManager, self).__init__(self, file_path)

    def get_config_obj(self):
        url1 = self.config["api"]["url1"]
        port1 = self.config["api"]["port1"]
        url2 = self.config["api"]["url2"]
        port2 = self.config["api"]["port2"]
        return APIConfig(url1, port1, url2, port2)

    class APIConfig:
        def __init__(self, url1, port1, url2, port2):
            self.url1 = url1
            self.port1 = port1
            self.url2 = url2
            self.port2 = port2
