#!/usr/bin/python
# {{ansible_managed}}
import sys
import urllib2

data = "".join(sys.stdin.readlines())

req = urllib2.Request('{{ item.url }}', data)
req.add_header('Content-Length', '%d' % len(data))
req.add_header('Content-Type', 'application/octet-stream')
res = urllib2.urlopen(req)

