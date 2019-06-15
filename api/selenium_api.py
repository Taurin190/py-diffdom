# -*- coding:utf-8 -*-
from selenium import webdriver


class SeleniumAPI:
    def __init__(self, url):
        super(SeleniumAPI, self).__init__(url)
        self.driver = webdriver.Chrome()

    def get_html(self):
        self.driver.get(self.url)
        return self.driver.page_source
