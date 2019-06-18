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
import os


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
        if config.type == "selenium":
            api = sapi.SeleniumAPI()
        else:
            api = rapi.RequestsAPI()
        return api

    @staticmethod
    def get_url_lists(file_path1, file_path2):
        current_path = os.getcwd()
        list1 = URLListReader.get_url_list(current_path + file_path1)
        list2 = URLListReader.get_url_list(current_path + file_path2)
        return [list1, list2]

    def __del__(self):
        end_time = time.time()
        print("diff check end: execution time[{:.5g} sec]".format(end_time - self.start_time))

    def exec(self):
        url_lists = DiffChecker.get_url_lists("/config/url_list1.txt", "/config/url_list2.txt")
        self.compare_from_url_lists(url_lists[0], url_lists[1])
        print("create domain")
        print("execute diff check")

    def compare_from_url_lists(self, url_list1, url_list2):
        for i in range(len(url_list1)):
            self.compare_urls(url_list1[i], url_list2[i])

    def compare_urls(self, url1, url2):
        config = acm.APIConfigManager("/config/api.conf").get_config_obj()
        api_connector = DiffChecker.get_api_connector(config)
        html1 = api_connector.get_html(url1)
        html2 = api_connector.get_html(url2)
        s1 = BeautifulSoup(html1, "html.parser")
        s2 = BeautifulSoup(html2, "html.parser")
