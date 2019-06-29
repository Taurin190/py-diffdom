# -*- coding:utf-8 -*-
import os
import time
from bs4 import BeautifulSoup

from api.requests_api import RequestsAPI
from api.selenium_api import SeleniumAPI
from config.url_list_reader import URLListReader
from config.db_config_manager import DBConfigManager
from config.api_config_manager import APIConfigManager
from repository.mongo_database import MongoDatabase
from repository.file_database import FileDatabase
from domain.dom_diff import DomDiff
from domain.line_diff import LineDiff
from domain.json_diff import JsonDiff


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
            api = SeleniumAPI()
        else:
            api = RequestsAPI()
        return api

    @staticmethod
    def get_url_lists(file_path1, file_path2):
        current_path = os.getcwd()
        list1 = URLListReader.get_url_list(current_path + file_path1)
        list2 = URLListReader.get_url_list(current_path + file_path2)
        return [list1, list2]

    @staticmethod
    def get_diff_tool(config):
        if config.type == "dom":
            diff_tool = DomDiff()
        elif config.type == "line":
            diff_tool = LineDiff()
        elif config.type == "json":
            diff_tool = JsonDiff()
        else:
            diff_tool = DomDiff()
        return diff_tool

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
        config = APIConfigManager("/config/api.conf").get_config_obj()
        api_connector = DiffChecker.get_api_connector(config)
        html1 = api_connector.get_html(url1)
        html2 = api_connector.get_html(url2)
        s1 = BeautifulSoup(html1, "html.parser")
        s2 = BeautifulSoup(html2, "html.parser")
        self.compare_parsed_html(s1, s2)

    def compare_parsed_html(self, s1, s2):
        self.is_same_dom(s1, s2, 0)

    def is_same_dom(self, s1, s2, nest):
        # s1, s2の両方がcontentsを持ってない場合は、s1, s2を比較して結果を返す
        if not hasattr(s1, 'contents') and not hasattr(s2, 'contents'):
            if s1 == s2:
                return True
            else:
                print(" " * nest + "+ " + str(s1))
                print(" " * nest + "- " + str(s2))
                return False
        # s1, s2のどちらかのみがcontentsを持ってない場合は、異なる
        elif not hasattr(s1, 'contents') or not hasattr(s2, 'contents'):
            print(" " * nest + "+ " + str(s1))
            print(" " * nest + "- " + str(s2))
            return False

        if len(s1.contents) == len(s2.contents):
            has_error = True
            for i in range(len(s1.contents)):
                if s1.contents[i].name:
                    html_tag = s1.contents[i].name
                    if s1.contents[i].get("id"):
                        html_tag += " id:" + s1.contents[i].get("id")
                    if s1.contents[i].get("class"):
                        html_tag += " class:" + str(s1.contents[i].get("class"))
                    print(" " * nest + html_tag)
                if not self.is_same_dom(s1.contents[i], s2.contents[i], nest+1):
                    has_error = False
            return has_error
        else:
            for s1_line in s1.contents:
                print(" " * nest + "+ " + str(s1_line))
            for s2_line in s2.contents:
                print(" " * nest + "- " + str(s2_line))
            return False
        return True




