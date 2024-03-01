#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : pmjs_test.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2024/2/29

from utils.quickjs_ctx import initGlobalThis
import pythonmonkey as pm
from pythonmonkey import eval as js_eval, require as js_require
# js_eval("globalThis._map = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';")
# CryptoJS = js_require('./crypto-js')
# text = CryptoJS.MD5('123456').toString()
# print('md5 text:',text)
# text = CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse('123456'))
# print('base64 text:',text)

initGlobalThis(pm)
js_eval("globalThis._map = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';")
CryptoJS = js_require('./drpy_lib')
# text = CryptoJS.MD5('123456').toString()
# print('md5 text:',text)
# text = CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse('123456'))
# print('base64 text:',text)

text = CryptoJS.md5('123456')
print('md5 text:',text)

text = CryptoJS.base64Encode('123456')
print('base64 text:',text)

text = CryptoJS.CryptoJS.MD5('123456').toString()
print('md5 text:',text)

# import pythonmonkey as pm
#
# print(pm.__version__)
# CryptoJS = pm.require('./node_modules/crypto-js')
# # print(CryptoJS.MD5)
#
# text = CryptoJS.MD5('123456').toString()
# print('md5 text:',text)
# text = CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse('123456'))
# print('base64 text:',text)