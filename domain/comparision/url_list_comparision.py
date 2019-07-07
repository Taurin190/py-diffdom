# -*- coding:utf-8 -*-
import os
from domain.comparision.comparision import Comparision
from config.url_list_reader import URLListReader

class URLListComparision(Comparision):
    def __init__(self, config, api, diff_tool):
        super().__init__(config, api, diff_tool)

    def get_comparable_htmls(self, **args):
        if not "url_list1" in args.keys() or not "url_list2" in args.keys():
            return
        comparable_html_list = []
        url_lists = self.get_url_lists(args.get("url_list1"), args.get("url_list2"))
        for i in range(len(url_lists[0])):
            html1 = self.api.get_html(url_lists[0][i])
            html2 = self.api.get_html(url_lists[1][i])
            comparable_html_list.append([html1, html2])
        return comparable_html_list

    def get_url_lists(self, file_path1, file_path2):
        current_path = os.getcwd()
        list1 = URLListReader.get_url_list(current_path + file_path1)
        list2 = URLListReader.get_url_list(current_path + file_path2)
        return [list1, list2]
