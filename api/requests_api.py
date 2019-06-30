# -*- coding:utf-8 -*-
import requests
from api import api


class RequestsAPI(api.API):
    def __init__(self):
        super().__init__()
        self.proxies = {}

    def get_html(self, url):
        response = requests.get(url)
        return response.text

    def set_proxy(self, proxy_url):
        self.proxies["http"] = proxy_url
