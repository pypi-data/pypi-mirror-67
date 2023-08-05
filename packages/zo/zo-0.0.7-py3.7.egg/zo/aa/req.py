# ! /usr/bin/python
# coding=utf-8
import re


def g_headers():
    aa = '''
:authority: fccid.io
:method: GET
:path: /AK8
:scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: en,en-US;q=0.9,zh-CN;q=0.8,zh;q=0.7
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36
'''
    aa = re.findall('(\w.*?):(.+)', aa)
    x = dict()
    for i in aa:
        x[i[0]] = re.sub('^ {1,}', '', i[1])
    for i in x:
        print('[%-20s] : %s' % (i, x[i]))
    print('- ' * 30)
    print(x)

g_headers()