# -*- coding:utf-8 -*-
from repository import database as db
from pymongo import MongoClient


class MongoDatabase(db.Database):
    def __init__(self, config):
        super().__init__(config)
        self.client = MongoClient(config["hostname"], int(config["port"]))
        self.collection = self.client[config["database"]][config["collection"]]

    def insert(self, document):
        self.collection.insert(document)

    def find_all(self):
        return self.collection.find({})

    def find_by_query(self, query):
        return self.collection.find(query)
