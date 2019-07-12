# -*- coding:utf-8 -*-
from domain.diff.diff import Diff


class MockDiff(Diff):
    def __init__(self, dummy_diff):
        super().__init__()
        self.dummy_diff = dummy_diff

    def compare(self, html1, html2):
        return self.dummy_diff
