from unittest import TestCase
from domain.diff.dom_diff import DomDiff


class DomDiffTest(TestCase):
    def setUp(self):
        self.dom_diff = DomDiff()

    def test_compare_no_diff(self):
        html1 = "<html><body><h1>Hello World</h1></body></html>"
        html2 = "<html><body><h1>Hello World</h1></body></html>"
        self.assertEqual("", self.dom_diff.compare(html1, html2))

    def test_compare_h1_diff(self):
        html1 = "<html><body><h1>Hello World</h1></body></html>"
        html2 = "<html><body><h1>Hello Hello</h1></body></html>"
        self.assertEqual("html > body > h1\n+ Hello World\n- Hello Hello\n", self.dom_diff.compare(html1, html2))

    def test_compare_h2_diff(self):
        html1 = "<html><body><h1>Hello World</h1><div><h2>Hoge Hoge</h2></div></body></html>"
        html2 = "<html><body><h1>Hello World</h1><div><h2>Fuga Fuga</h2></div></body></html>"
        self.assertEqual("html > body > div > h2\n+ Hoge Hoge\n- Fuga Fuga\n", self.dom_diff.compare(html1, html2))
