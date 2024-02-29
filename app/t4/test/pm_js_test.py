#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : pm_js_test.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2024/2/29

import pythonmonkey as pm
from pythonmonkey import eval as js_eval, require as js_require

js_eval("console.log")('hello, world')

# cheerio = js_require('./cheerio.min')
# print(cheerio)
# url = 'a=1&{{fl}}'
# new_url = cheerio.jinja2(url, {"fl": "test_ok"})
# print(new_url)

with open('crypto-hiker.js',encoding='utf-8') as f:
    code = f.read()
# print(code)
CryptoJS = js_eval(code)
#
print(1111)
print(CryptoJS)



# CryptoJS = js_require('./crypto')
CryptoJS = js_require('./crypto-js')
# CryptoJS = js_require('./crypto-hiker')
# CryptoJS = js_require('./crypto-js.min')
print(type(CryptoJS))
print(dir(CryptoJS))
print(type(CryptoJS.MD5))
print(type(CryptoJS.root))
globalThis = pm.eval("globalThis;", {})
print('globalThis:',type(globalThis))
# print('globalThis.CryptoJS:',globalThis.CryptoJS)
# print(CryptoJS.SHA256('Hello, World!').toString())
print(222)
text = CryptoJS.MD5('123456').toString()
# text = pm.eval("CryptoJS.MD5('123456').toString()")
# text = pm.eval("globalThis.CryptoJS.MD5('123456').toString()")
print('md5 text:',text)
text = CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse('123456'))
print('base64 text:',text)

# sha256 = js_require("./sha256")

# print(sha256("Hello, World!")) # this outputs dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f

# gbkTool = js_require('./gbk')
# print(gbkTool)
# strTool = gbkTool()
# input = strTool.encode('斗罗大陆')
# print(input)

# 模板 = js_require('./模板')
# # print(模板)
# muban = 模板.getMubans()
# print(muban)