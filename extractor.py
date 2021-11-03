#!/usr/bin/env python3
import re

unames=[]
co=open('/Users/jesherjoshua/Documents/jesher/Programming/Python/secrets/_chat.txt')
ig_uname_regex =re.compile(r'@(?:(?:[\w][\.]{0,1})*[\w]){1,30}')
for i in co:
    if len(ig_uname_regex.findall(i))==0 or ig_uname_regex.findall(i)[0][1:].isdigit():continue
    else:
        unames.append(ig_uname_regex.findall(i)[0])
unames_str='\n'.join(unames)
print(unames_str)