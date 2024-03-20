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
    ctx.module(qjs_module_muban)
    muban = ctx.get('muban')
    print(muban)
