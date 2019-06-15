# -*- coding:utf-8 -*-


class API:
    def __init__(self, url):
        self.url = url

    @abstractmethod
    def get_html(self):
        raise NotImpementedError()
