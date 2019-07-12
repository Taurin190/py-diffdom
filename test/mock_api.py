# -*- coding:utf-8 -*-
from api import api


class MockAPI(api.API):
    def __init__(self, dummy_response):
        super().__init__()
        self.proxies = {}
        self.dummy_response = dummy_response

    def get_html(self, url):
        return self.dummy_response

    def set_proxy(self, proxy_url):
        self.proxies["http"] = proxy_url