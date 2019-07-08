# -*- coding:utf-8 -*-
from domain.comparision.comparision import Comparision


class URLComparision(Comparision):
    def __init__(self, config, api, diff_tool):
        super().__init__(config, api, diff_tool)

    def get_comparable_htmls(self, **args):
        if not ["url1", "url2"] in args.keys():
            return
        url1 = args["url1"]
        url2 = args["url2"]
        html1 = self.api.get_html(url1)
        html2 = self.api.get_html(url2)
        return [html1, html2]

    def compare_with_diff_tool(self, htmls):
        self.diff_tool.compare(htmls[0], htmls[1])
