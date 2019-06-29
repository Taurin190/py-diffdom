# -*- coding:utf-8 -*-
from domain.diff import Diff
from bs4 import BeautifulSoup


class DomDiff(Diff):
    def __init__(self):
        super().__init__()
        self.result_text = ""

    def compare(self, html1, html2):
        s1 = BeautifulSoup(html1, "html.parser")
        s2 = BeautifulSoup(html2, "html.parser")
        self._is_same_dom(s1, s2, 0)
        return self.result_text

    def _is_same_dom(self, s1, s2, nest):
        # s1, s2の両方がcontentsを持ってない場合は、s1, s2を比較して結果を返す
        if not hasattr(s1, 'contents') and not hasattr(s2, 'contents'):
            if s1 == s2:
                return True
            else:
                self.result_text += " " * nest + "+ " + str(s1)
                self.result_text += " " * nest + "- " + str(s2)
                print(" " * nest + "+ " + str(s1))
                print(" " * nest + "- " + str(s2))
                return False
        # s1, s2のどちらかのみがcontentsを持ってない場合は、異なる
        elif not hasattr(s1, 'contents') or not hasattr(s2, 'contents'):
            self.result_text += " " * nest + "+ " + str(s1)
            self.result_text += " " * nest + "- " + str(s2)
            print(" " * nest + "+ " + str(s1))
            print(" " * nest + "- " + str(s2))
            return False

        if len(s1.contents) == len(s2.contents):
            has_error = True
            for i in range(len(s1.contents)):
                if s1.contents[i].name:
                    html_tag = s1.contents[i].name
                    if s1.contents[i].get("id"):
                        html_tag += " id:" + s1.contents[i].get("id")
                    if s1.contents[i].get("class"):
                        html_tag += " class:" + str(s1.contents[i].get("class"))
                    self.result_text += " " * nest + html_tag
                    print(" " * nest + html_tag)
                if not self.is_same_dom(s1.contents[i], s2.contents[i], nest+1):
                    has_error = False
            return has_error
        else:
            for s1_line in s1.contents:
                self.result_text += " " * nest + "+ " + str(s1_line)
                print(" " * nest + "+ " + str(s1_line))
            for s2_line in s2.contents:
                self.result_text += " " * nest + "+ " + str(s2_line)
                print(" " * nest + "- " + str(s2_line))
            return False

