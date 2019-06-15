# -*- coding:utf-8 -*-


class URLListReader:
    def __init__(self, conf_path):
        pass

    @staticmethod
    def get_url_list(file_path):
        url_list = []
        with open(file_path) as f:
            for line in f.readlines():
                url_list.append(line)
        return url_list

