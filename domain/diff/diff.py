# -*- coding:utf-8 -*-
from abc import abstractmethod


# 2つのhtmlファイルが与えられた時に、差分を返す
# 差分を出す方法については、いくつかの方法で実現する
class Diff:
    def __init__(self):
        pass

    @abstractmethod
    def compare(self, html1, html2):
        raise NotImplementedError()
