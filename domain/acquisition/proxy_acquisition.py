# -*- coding:utf-8 -*-
from domain.acquisition.acquisition import Acquisition


class ProxyAcquisition(Acquisition):
    def __init__(self, repository):
        super().__init__(repository)