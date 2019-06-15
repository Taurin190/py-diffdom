# -*- coding:utf-8 -*-
from selenium import webdriver
from api import api


class SeleniumAPI(api.API):
    def __init__(self, url):
        super().__init__(url)
        self.driver = webdriver.Chrome()

    def get_html(self):
        self.driver.get(self.url)
        return self.driver.page_source

    def __del__(self):
        self.driver.close()

