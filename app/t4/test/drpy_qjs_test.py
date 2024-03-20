#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : drpy_qjs_test.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2024/3/20

from quickjs import Context
from utils.quickjs_ctx import initContext

if __name__ == '__main__':
    ctx = Context()
    initContext(ctx, url='', prefix_code='true', env={}, getParams=lambda: {}, getCryptoJS=lambda: 'true')
    with open('qjs_module_muban.js', encoding='utf-8') as f:
        qjs_module_muban = f.read()
    with open('qjs_module_cheerio.js', encoding='utf-8') as f:
        qjs_module_cheerio = f.read()
    with open('qjs_module_gbk.js', encoding='utf-8') as f:
        qjs_module_gbk = f.read()
    with open('crypto-js.js', encoding='utf-8') as f:
        qjs_module_crypto = f.read()
    with open('qjs_module_drpy2.js', encoding='utf-8') as f:
        qjs_module_drpy2 = f.read()
    ctx.eval(qjs_module_muban)
    print(ctx.eval('模板.muban'))
    print(ctx.eval('typeof(模板)'))

    ctx.module(qjs_module_cheerio)
    print(ctx.eval('typeof cheerio.jinja2'))

    ctx.module(qjs_module_gbk)
    print('typeof gbkTool().encode:', ctx.eval('typeof gbkTool().encode'))

    ctx.module(qjs_module_crypto)
    print('typeof CryptoJS.enc.Utf8.parse:', ctx.eval('typeof CryptoJS.enc.Utf8.parse'))

    key = "SPKEY"
    ctx.module(
        qjs_module_drpy2 + '\nglobalThis.' + key + ' = { init, home, homeVod, category, detail, play, search, proxy, sniffer, isVideo};')
    print(ctx.eval('typeof globalThis.SPKEY.init'))
    test_rule_url = 'https://ghproxy.liuzhicong.com/https://github.com/hjdhnx/dr_py/raw/main/js/996%E5%BD%B1%E8%A7%86.js'
    ctx.set('test_rule_url', test_rule_url)
    print(ctx.eval('globalThis.SPKEY.init(test_rule_url)'))
    # print(ctx.eval('globalThis.SPKEY.home()'))
    # print(ctx.eval('globalThis.SPKEY.category(3,1,false,{})'))
    # print(ctx.eval('globalThis.SPKEY.detail("3$/detail/790.html")'))
    print(ctx.eval('globalThis.SPKEY.play("索尼","https://www.cs1369.com/play/790-1-1.html",[])'))
    # print(ctx.eval('globalThis.SPKEY.search("斗罗大陆",false,1)'))
