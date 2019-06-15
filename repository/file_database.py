# -*- coding:utf-8 -*-
from repository import database as db


class FileDatabase(db.Database):
    def __init__(self, config):
        super().__init__(config)

    def insert(self, document):
        pass

    def find_all(self):
        pass

    def find_by_query(self, query):
        pass