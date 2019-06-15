# -*- coding:utf-8 -*-
from abc import abstractmethod


class Database:
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def insert(self, document):
        raise NotImplementedError()

    @abstractmethod
    def find_all(self):
        raise NotImplementedError()

    @abstractmethod
    def find_by_query(self, query):
        raise NotImplementedError()
