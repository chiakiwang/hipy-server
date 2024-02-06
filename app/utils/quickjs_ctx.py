#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : quickjs_ctx.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/2/6

from core.logger import logger
from t4.base.htmlParser import jsoup
from utils.vod_tool import fetch, 重定向, toast, image
from utils.local_cache import local


def initContext(ctx, url, prefix_code, env, getParams, getCryptoJS):
    ctx.add_callable("getParams", getParams)
    ctx.add_callable("log", logger.info)
    ctx.add_callable("print", print)
    ctx.add_callable("fetch", fetch)
    ctx.eval("const console = {log};")
    ctx.add_callable("getCryptoJS", getCryptoJS)
    jsp = jsoup(url)
    ctx.add_callable("pdfh", jsp.pdfh)
    ctx.add_callable("pdfa", jsp.pdfa)
    ctx.add_callable("pd", jsp.pd)
    ctx.eval("var jsp = {pdfh, pdfa, pd};")
    ctx.add_callable("local_set", local.set)
    ctx.add_callable("local_get", local.get)
    ctx.add_callable("local_delete", local.delete)
    ctx.eval("const local = {get:local_get,set:local_set,delete:local_delete};")

    ctx.add_callable("重定向", 重定向)
    ctx.add_callable("toast", toast)
    ctx.add_callable("image", image)

    set_values = {
        'vipUrl': url,
        'realUrl': '',
        'input': url,
        'fetch_params': {'headers': {'Referer': url}, 'timeout': 10, 'encoding': 'utf-8'},
        'env': env,
        'params': getParams()
    }
    for key, value in set_values.items():
        if isinstance(value, dict):
            ctx.eval(f'var {key} = {value}')
        else:
            ctx.set(key, value)

    ctx.eval(prefix_code)
    return ctx
