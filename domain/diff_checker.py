# -*- coding:utf-8 -*-
import os
import time
import configparser

from api.requests_api import RequestsAPI
from api.selenium_api import SeleniumAPI
from config.url_list_reader import URLListReader
from repository.mongo_database import MongoDatabase
from repository.file_database import FileDatabase
from domain.diff.dom_diff import DomDiff
from domain.diff.line_diff import LineDiff
from domain.diff.json_diff import JsonDiff
from domain.comparision.url_list_comparision import URLListComparision


class DiffChecker:
    def __init__(self):
        self.start_time = time.time()
        print("start diff check tool")
        current_path = os.getcwd()
        self.config = configparser.ConfigParser()
        self.config.read(current_path + "/config/app.conf")
        print("create repository")
        self.repository = DiffChecker.get_repository(self.config["database"])

    @staticmethod
    def get_repository(config):
        if config["type"] == "mongo":
            repository = MongoDatabase(config)
        else:
            repository = FileDatabase(config)
        return repository

    @staticmethod
    def get_api_connector(config):
        if config["type"] == "selenium":
            api = SeleniumAPI()
        else:
            api = RequestsAPI()
        return api

    @staticmethod
    def get_diff_tool(config):
        if config["app"]["diff_type"] == "dom":
            diff_tool = DomDiff(config["diff"])
        elif config["app"]["diff_type"] == "line":
            diff_tool = LineDiff()
        elif config["app"]["diff_type"] == "json":
            diff_tool = JsonDiff()
        else:
            diff_tool = DomDiff(config["diff"])
        return diff_tool

    @staticmethod
    def get_html_files(config, api):
        url_lists_acquire = URLListComparision(api)
        return url_lists_acquire.get_comparable_htmls(url_list1=config["url_list1"], url_list2=config["url_list2"])

    @staticmethod
    def get_comparision_tool(config, api, diff_tool):
        comparision = URLListComparision(config, api, diff_tool)
        return comparision



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
        api = DiffChecker.get_api_connector(self.config["api"])
        diff_tool = DiffChecker.get_diff_tool(self.config)
        html_lists = DiffChecker.get_html_files(self.config["api"], api)
        for htmls in html_lists:
            diff_tool.compare(htmls[0], htmls[1])

