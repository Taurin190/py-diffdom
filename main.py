#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from domain.diff_checker import DiffChecker


def main(*arg):
    diff_check = DiffChecker()
    diff_check.exec(*arg)


if __name__ == '__main__':
    args = sys.argv
    diff_check = DiffChecker()
    diff_check.exec(*args)
