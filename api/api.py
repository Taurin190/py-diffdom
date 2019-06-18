# -*- coding:utf-8 -*-
from abc import abstractmethod


class API:
    def __init__(self):
        pass

    @abstractmethod
    def get_html(self, url):
        raise NotImplementedError()
