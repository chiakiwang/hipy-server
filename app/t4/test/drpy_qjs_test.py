#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : drpy_qjs_test.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2024/3/20

from quickjs import Context

if __name__ == '__main__':
    ctx = Context()
    with open('qjs_module_muban.js', encoding='utf-8') as f:
        qjs_module_muban = f.read()
    with open('qjs_module_cheerio.js', encoding='utf-8') as f:
        qjs_module_cheerio = f.read()
    # ctx.module(qjs_module_muban+'\nglobalThis.muban = muban;')
    ctx.module(qjs_module_muban + '\nglobalThis.muban = muban;')
    print(ctx.eval('muban.mxpro.一级'))

    # ctx.module(qjs_module_cheerio.replace('export','globalThis.cheerio =') + '\nglobalThis.jinja2 = dh;')
    # ctx.module(qjs_module_cheerio.replace('export','globalThis.cheerio =') + '\nglobalThis.jinja2 = dh;')
    ctx.module(qjs_module_cheerio + '\nglobalThis.jinja2 = dh;')
    print(ctx.eval('typeof jinja2'))
