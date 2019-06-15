# -*- coding:utf-8 -*-
import time
from repository import mongo_database as mdb
from repository import file_database as fdb
from api import requests_api as rapi
from api import selenium_api as sapi
from config import url_list_reader as ulr
from config import db_config_manager as dcm
from config import api_config_manager as acm


class DiffCheck:
    def __init__(self):
        self.start_time = time.time()
        print("start diff check tool")
        db_config = dcm.DBConfigManager("./config/database.conf").get_config_obj()
        api_config = acm.DBConfigManager("./config/api.conf").get_config_obj()
        print("create repository")
        self.repository = DiffCheck.get_repository(db_config)
        print("create api connector")
        self.api = DiffCheck.get_api_connector(api_config)

    @staticmethod
    def get_repository(config):
        if config.type == "mongo":
            repository = mdb.MongoDatabase(config)
        else:
            repository = fdb.FileDatabase(config)
        return repository

    @staticmethod
    def get_api_connector(config):
        if config.type == "selenium":
            api = sapi.SeleniumAPI(config)
        else:
            api = rapi.RequestsAPI(config)
        return api

    @staticmethod
    def get_url_lists(file_path1, file_path2):
        list1 = ulr.URLListReader.get_url_list(file_path1)
        list2 = ulr.URLListReader.get_url_list(file_path2)
        return [list1, list2]

    def __del__(self):
        end_time = time.time()
        print("diff check end: execution time[{:.5g} sec]".format(end_time - self.start_time))

    def exec(self):
        url_lists = DiffCheck.get_url_lists("", "")
        self.compare_from_url_lists(url_lists[0], url_lists[1])
        print("create domain")
        print("execute diff check")

    def compare_from_url_lists(self, url_list1, url_list2):
        for i in range(len(url_list1)):
            self.compare_urls(url_list1[i], url_list2[2])

    def compare_urls(self, url1, url2):
        pass
