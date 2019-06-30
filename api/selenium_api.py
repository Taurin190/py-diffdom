# -*- coding:utf-8 -*-
from selenium import webdriver
from api import api


class SeleniumAPI(api.API):
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Chrome()

    def get_html(self, url):
        self.driver.get(url)
        return self.driver.page_source

    def set_proxy(self, proxy_url):
        pass

    def __del__(self):
        self.driver.close()

