# -*- coding:utf-8 -*-
from domain.acquisition.acquisition import Acquisition


class URLListAcquisition(Acquisition):
    def __init__(self, repository):
        super().__init__(repository)

    def get_comparable_htmls(self, **args):
        if not ["url_lis1", "url_list2"] in args.keys():
            return
        comaparable_html_list = []
        url_list1 = args["url_list1"]
        url_list2 = args["url_list2"]
        for i in range(len(url_list1)):
            html1 = self.api.get_html(url_list1[i])
            html2 = self.api.get_html(url_list2[i])
            comaparable_html_list.append([html1, html2])
        return comaparable_html_list
