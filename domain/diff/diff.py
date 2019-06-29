# -*- coding:utf-8 -*-
from abc import abstractmethod


class Diff:
    def __init__(self):
        pass

    @abstractmethod
    def compare(self, html1, html2):
        raise NotImplementedError()
