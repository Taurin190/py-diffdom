# -*- coding:utf-8 -*-
from domain.comparision import Comparision


class ProxyComparision(Comparision):
    def __init__(self, repository):
        super().__init__(repository)