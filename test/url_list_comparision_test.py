import sys
from io import StringIO
from unittest import TestCase
from domain.comparision.url_list_comparision import URLListComparision
from exception.invalid_argument_error import InvalidArgumentError

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

    def test_get_comparable_htmls_exception(self):
        diff_tool = MockDiff("aaa")
        api = MockAPI("")
        comparison_tool = URLListComparision("", api, diff_tool)
        try:
            comparison_tool.compare_with_diff_tool(url_list1="aaa.txt")
        except InvalidArgumentError as e:
            self.assertEqual("Argument is not valid", str(e))
        else:
            self.fail("Not correct exception occur in get_comparable_htmls")





