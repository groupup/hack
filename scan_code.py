#!/bin/env python
# -*- coding: utf-8 -*-
import re
import os
import sys

functions = []
functions.append("[\@\ \(]+system\(")
functions.append("[\@\ \(]+exec\(")
functions.append("[\@\ \(]+passthru\(")
functions.append("[\@\ \(]+shell_exec\(")
functions.append("[\@\ \(]+eval\(")

def scan_file(file_name,functions):
    if not os.path.isfile(file_name):
        return
    has = False
    s = open(file_name).read()
    for function in functions:
        function = function.strip()
        m = re.compile(function)
        result = m.findall(s)
        if result:
            has = True
            print "File: %s" % file_name
            for i in result:
                print i
    if has:
        print "\n\n"

def get_file(path,ext):
    file_list = []
    ext = ext.strip()
    for dirpath,dirnames,filenames in os.walk(path):
        for name in filenames:
            sufix = os.path.splitext(name)[1][1:]
            if sufix == ext:
                t = os.path.join(dirpath,name)
                file_list.append(t)
    return file_list

def scan(path,functions,ext):
    if os.path.isfile(path):
        scan_file(path,functions)
    elif os.path.exists(path):
        files = get_file(path,ext)
        for f in files:
            scan_file(f,functions)

def main():
    if os.path.lexists(sys.argv[1]):
        scan(sys.argv[1],functions,"php")

if __name__ == "__main__":
    main()
