#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time


def main():
    start_time = time.time()
    print("main start")
    print("read config file")
    print("create repository")
    print("create api connector")
    print("create domain")
    print("execute diff check")
    end_time = time.time()
    print("main end: execution time[{:.5g} sec]".format(end_time - start_time))


if __name__ == '__main__':
    main()
