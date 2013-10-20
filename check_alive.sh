#!/bin/bash
#this is a scanner to check domain is alive
for i in `cat $1`;do
    nslookup $i.$2 | grep Name > /dev/null;
    if [ $? -eq 0 ];then
        nslookup $i.$2 | grep  "Name"
#        nslookup $i.$2 
    fi
done
