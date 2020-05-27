# coding=utf-8
import re


with open('gothic.css') as f:
    content = f.read()


regex = re.compile('url\((.*?)\)')
result = list(set(regex.findall(content)))

for i in result:
    print 'wget "%s"' % i
