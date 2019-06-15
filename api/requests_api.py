# -*- coding:utf-8 -*-
import requests
from api import api


class RequestsAPI(api.API):
    def __init__(self, url):
        super().__init__(url)

    def get_html(self):
        response = requests.get(self.url)
        return response.text
