# -*- coding:utf-8 -*-
from repository import database as db


class MongoDatabase(db.Database):
    def __init__(self, config):
        super().__init__(config)
