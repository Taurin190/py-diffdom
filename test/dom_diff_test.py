from unittest import TestCase
from domain.diff.dom_diff import DomDiff


class DomDiffTest(TestCase):
    def test_compare_no_diff(self):
        dom_diff = DomDiff()
        html1 = "<html><body><h1>Hello World</h1></body></html>"
        html2 = "<html><body><h1>Hello World</h1></body></html>"
        self.assertEqual("", dom_diff.compare(html1, html2))

    def test_compare_h1_diff(self):
        dom_diff = DomDiff()
        html1 = "<html><body><h1>Hello World</h1></body></html>"
        html2 = "<html><body><h1>Hello Hello</h1></body></html>"
        self.assertEqual("html > body > h1\n+ Hello World\n- Hello Hello\n", dom_diff.compare(html1, html2))
