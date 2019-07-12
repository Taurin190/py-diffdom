from unittest import TestCase
from domain.comparision.url_list_comparision import URLListComparision


class DomDiffTest(TestCase):
    def test_失敗するテスト(self):
        self.assertEquals("","失敗")