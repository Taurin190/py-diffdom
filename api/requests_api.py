# -*- coding:utf-8 -*-
import requests


class RequestsAPI:
    def __init__(self, url):
        super(SeleniumAPI, self).__init__(url)

    def get_html(self):
        response = requests.get(self.url)
        return response.text
