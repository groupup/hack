#!/bin/env python
# -*- coding: utf-8 -*-
# 虚拟机装机阶段的初始化脚本。
# 此脚本运行阶段机器不能解析域名,但是可以访问外网.

import json
import re
import urllib
import urllib2
import threading
import thread
import subprocess
import httplib

def get_lines(file_name):
    f = open(file_name)
    return f.readlines()
    
def parse_robots(site,reg):
    site = site.strip()
    conn = httplib.HTTPConnection(site,80,timeout=5)
    conn.request("GET","/robots.txt")
    response = conn.getresponse()
    data = response.read()
    if response.status != 200:
        thread.exit_thread()
    for i in reg:
        m = re.search(i,data)
        if m:
            print "%s %s" % (site, i)
            thread.exit_thread()
    f = open("robots.txt","w+")
    f.write("site %s\n" % site)
    f.write(data)
    f.write("\n\n")
    thread.exit_thread()

def main():
    sites = get_lines("robots")
    reg = []
    reg.append("wp-admin")
    reg.append("Discuz")
    thread_list = []
    for i in sites:
        t = threading.Thread(target = parse_robots, args = (i,reg))
        thread_list.append(t)
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()


if __name__ == '__main__':
    main()
