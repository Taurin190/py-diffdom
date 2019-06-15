# -*- coding:utf-8 -*-


class Database:
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def connect(self):
        raise NotImpementedError()

    @abstractmethod
    def insert(self):
        raise NotImpementedError()

    @abstractmethod
    def find_all(self):
        raise NotImpementedError()

    @abstractmethod
    def find_by_query(self, query):
        raise NotImpementedError()
