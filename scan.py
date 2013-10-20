#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def scan_plugin(url,body):
    m = re.search('<input[^>]+type=[\'"]*file[\'"]*',body)
    if m:
        print m

if __name__ == '__main__':
    print "yes"
