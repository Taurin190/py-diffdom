# -*- coding:utf-8 -*-
from domain.acquisition.acquisition import Acquisition


class ProxyAcquisition(Acquisition):
    def __init__(self, api):
        super().__init__(api)

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

