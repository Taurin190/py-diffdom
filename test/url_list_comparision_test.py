import sys
from io import StringIO
from unittest import TestCase
# from test.support import captured_stdout
from domain.comparision.url_list_comparision import URLListComparision

from test.mock_diff_tool import MockDiff
from test.mock_api import MockAPI


class DomDiffTest(TestCase):
    def test_get_comparable_htmls(self):
        org_stdout, sys.stdout = sys.stdout, StringIO()
        diff_tool = MockDiff("aaa")
        api = MockAPI("")
        comparison_tool = URLListComparision("", api, diff_tool)
        comparison_tool.compare_with_diff_tool(url_list1="list1.txt", url_list2="list2.txt")
        sys.stdout = org_stdout
        self.assertEqual("", sys.stdout.getvalue())
