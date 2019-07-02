from unittest import TestCase
from domain.diff.dom_diff import DomDiff


class DomDiffTest(TestCase):
    def test_失敗するテスト実施(self):
        self.assertEqual("", "失敗")
