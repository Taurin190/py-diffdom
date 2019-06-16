# -*- coding:utf-8 -*-
import time
from repository.mongo_database import MongoDatabase
from repository.file_database import FileDatabase
from api import requests_api as rapi
from api import selenium_api as sapi
from config.url_list_reader import URLListReader
from config.db_config_manager import DBConfigManager
from config import api_config_manager as acm
from bs4 import BeautifulSoup


class DiffChecker:
    def __init__(self):
        self.start_time = time.time()
        print("start diff check tool")
        db_config = DBConfigManager("/config/database.conf").get_config_obj()
        print("create repository")
        self.repository = DiffChecker.get_repository(db_config)

    @staticmethod
    def get_repository(config):
        if config.type == "mongo":
            repository = MongoDatabase(config)
        else:
            repository = FileDatabase(config)
        return repository

    @staticmethod
    def get_api_connector(config):
        config = acm.APIConfigManager("/config/api.conf").get_config_obj()
        if config.type == "selenium":
            api = sapi.SeleniumAPI(config)
        else:
            api = rapi.RequestsAPI(config)
        return api

    @staticmethod
    def get_url_lists(file_path1, file_path2):
        list1 = URLListReader.get_url_list(file_path1)
        list2 = URLListReader.get_url_list(file_path2)
        return [list1, list2]

    def __del__(self):
        end_time = time.time()
        print("diff check end: execution time[{:.5g} sec]".format(end_time - self.start_time))

    def exec(self):
        url_lists = DiffChecker.get_url_lists("", "")
        self.compare_from_url_lists(url_lists[0], url_lists[1])
        print("create domain")
        print("execute diff check")

    def compare_from_url_lists(self, url_list1, url_list2):
        for i in range(len(url_list1)):
            self.compare_urls(url_list1[i], url_list2[2])

    def compare_urls(self, url1, url2):
        print("create api connector")
        html1 = DiffChecker.get_api_connector(url1).get_html()
        html2 = DiffChecker.get_api_connector(url2).get_html()
        s1 = BeautifulSoup(html1, "html.parser")
        s2 = BeautifulSoup(html2, "html.parser")
