# -*- coding:utf-8 -*-
from domain.acquisition.acquisition import Acquisition


class URLAcquisition(Acquisition):
    def __init__(self, api):
        super().__init__(api)

    def get_comparable_htmls(self, **args):
        if not ["url1", "url2"] in args.keys():
            return
        url1 = args["url1"]
        url2 = args["url2"]
        html1 = self.api.get_html(url1)
        html2 = self.api.get_html(url2)
        return [html1, html2]
