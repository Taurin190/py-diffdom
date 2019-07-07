# -*- coding:utf-8 -*-
from domain.comparision.comparision import Comparision


class ProxyComparision(Comparision):
    def __init__(self, config, api, diff_tool):
        super().__init__(config, api, diff_tool)

    def get_comparable_htmls(self, **args):
        if not ["url", "proxy1", "proxy2"] in args.keys():
            return
        url = args["url"]
        proxy1 = args["proxy1"]
        proxy2 = args["proxy2"]
        html1 = self._get_html_from_api(url, proxy1)
        html2 = self._get_html_from_api(url, proxy2)
        return [html1, html2]

    def _get_html_from_api(self, url, proxy):
        self.api.set_proxy(proxy)
        return self.api.get_html(url)

