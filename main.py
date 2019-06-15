#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from config import db_config_manager


def main():
    start_time = time.time()
    print("main start")
    print("read config file")
    db_config = db_config_manager.DBConfigManager("./config/database.conf").get_config_obj()
    api_config = db_config_manager.DBConfigManager("./config/api.conf").get_config_obj()
    print("create repository")

    print("create api connector")
    print("create domain")
    print("execute diff check")
    end_time = time.time()
    print("main end: execution time[{:.5g} sec]".format(end_time - start_time))


if __name__ == '__main__':
    main()
