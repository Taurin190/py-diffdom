# -*- coding:utf-8 -*-
from abc import abstractmethod


class Comparision:
    def __init__(self, config, api, diff_tool):
        self.api = api
        self.config = config
        self.diff_tool = diff_tool

    @abstractmethod
    def get_comparable_htmls(self, **args):
        raise NotImplementedError()

