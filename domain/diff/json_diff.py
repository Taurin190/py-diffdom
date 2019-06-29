# -*- coding:utf-8 -*-
from domain.diff.diff import Diff


class JsonDiff(Diff):
    def __init__(self):
        super().__init__()

    def compare(self, html1, html2):
        pass
