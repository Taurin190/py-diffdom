# -*- coding:utf-8 -*-
from abc import abstractmethod


class Acquisition:
    def __init__(self, api):
        self.api = api

    @abstractmethod
    def get_comparable_htmls(self, **args):
        raise NotImplementedError()

