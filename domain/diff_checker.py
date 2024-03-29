# -*- coding:utf-8 -*-
import os
import time
import configparser

from api.requests_api import RequestsAPI
from api.selenium_api import SeleniumAPI
from config.url_list_reader import URLListReader
from domain.diff.dom_diff import DomDiff
from domain.diff.line_diff import LineDiff
from domain.diff.json_diff import JsonDiff
from domain.comparision.url_list_comparision import URLListComparision


class DiffChecker:
    def __init__(self):
        self.start_time = time.time()
        self.is_normal_end = True

    @staticmethod
    def show_usage():
        print("diffdom is a tool for compare html comparing dom structure\n\n"
              "Usage:\n"
              "  diffdom [config file]")

    @staticmethod
    def show_config_usage():
        print("Please take a look available parameters for the config file\n\n"
              "Params:\n"
              "[app](arbitrary)\n"
              "diff_type : \n"
              "  It is how to get diff. you can choose from \'dom\', \'line\', \'json\'\n"
              "  default is \'dom\'")

    @staticmethod
    def get_api_connector(config):
        if not "api" in config.keys():
            return RequestsAPI()
        if config["api"]["type"] == "selenium":
            return SeleniumAPI()
        return RequestsAPI()

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
        if self.is_normal_end:
            end_time = time.time()
            print("diff check end: execution time[{:.5g} sec]".format(end_time - self.start_time))

    def exec(self, *args):
        if len(args) < 2:
            DiffChecker.show_usage()
            self.is_normal_end = False
            exit(1)
        if args[1] == "help":
            DiffChecker.show_usage()
            DiffChecker.show_config_usage()
            self.is_normal_end = False
            exit(1)
        arg_config = args[1]
        current_path = os.getcwd()
        config = configparser.ConfigParser()
        config.read(current_path + "/" + arg_config)
        api = DiffChecker.get_api_connector(config)
        diff_tool = DiffChecker.get_diff_tool(config)
        comparision_tool = DiffChecker.get_comparision_tool(config["app"], api, diff_tool)
        comparision_tool.compare_with_diff_tool(url_list1=config["api"]["url_list1"], url_list2=config["api"]["url_list2"])


