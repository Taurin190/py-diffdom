# -*- coding:utf-8 -*-
from abc import abstractmethod

class API:
    def __init__(self, url):
        self.url = url

    @abstractmethod
    def get_html(self):
        raise NotImplementedError()
