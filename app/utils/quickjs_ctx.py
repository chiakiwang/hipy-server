#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : quickjs_ctx.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/2/6
import ujson

# from core.logger import logger
from t4.base.htmlParser import jsoup
from utils.vod_tool import fetch, req, 重定向, toast, image
from urllib.parse import urljoin
from utils.local_cache import local


def initContext(ctx, url, prefix_code, env, getParams, getCryptoJS):
    """
    qjs引擎的注入函数
    @param ctx:
    @param url:
    @param prefix_code:
    @param env:
    @param getParams:
    @param getCryptoJS:
    @return:
    """

    def toJsObJect(any):
        if isinstance(any, dict) or isinstance(any, list):
            return ctx.parse_json(ujson.dumps(any, ensure_ascii=False))
        return any

    def toDict(_object):
        return ujson.loads(_object.json())

    def empty(*args):
        pass

    ctx.add_callable("getParams", getParams)
    # ctx.add_callable("log", logger.info)
    ctx.add_callable("log", print if env.get('debug') else empty)
    ctx.add_callable("print", print if env.get('debug') else empty)
    ctx.add_callable("fetch", fetch)
    # ctx.add_callable("req", lambda _url, _object: ctx.parse_json(ujson.dumps(req(_url, _object))))
    ctx.add_callable("req", lambda _url, _object: toJsObJect(req(_url, toDict(_object))))
    ctx.add_callable("urljoin", urljoin)
    ctx.add_callable("joinUrl", urljoin)
    ctx.eval("const console = {log};")
    ctx.add_callable("getCryptoJS", getCryptoJS)
    jsp = jsoup(url)
    ctx.add_callable("pdfh", jsp.pdfh)
    # ctx.add_callable("pdfa", lambda html, parse: ctx.parse_json(ujson.dumps(jsp.pdfa(html, parse))))
    ctx.add_callable("pdfa", lambda html, parse: toJsObJect(jsp.pdfa(html, parse)))
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


def initGlobalThis(ctx):
    """
    pythonmonkey引擎的注入函数
    @param ctx:
    @return:
    """
    globalThis = ctx.eval("globalThis;")
    _url = 'https://www.baidu.com'
    globalThis.fetch_params = {'headers': {'Referer': _url}, 'timeout': 10, 'encoding': 'utf-8'}
    globalThis.log = print
    globalThis.print = print
    globalThis.req = req

    def pdfh(html, parse: str, base_url: str = ''):
        jsp = jsoup(base_url)
        return jsp.pdfh(html, parse, base_url)

    def pd(html, parse: str, base_url: str = ''):
        jsp = jsoup(base_url)
        return jsp.pd(html, parse)

    def pdfa(html, parse: str):
        jsp = jsoup()
        return jsp.pdfa(html, parse)

    def local_get(_id, key, value='', *args):
        print('local_get:', _id, key, value)
        return local.get(_id, key, value)

    def local_set(_id, key, value):
        return local.set(_id, key, value)

    def local_delete(_id, key):
        return local.delete(_id, key)

    globalThis.pdfh = pdfh
    globalThis.pdfa = pdfa
    globalThis.pd = pd
    globalThis.joinUrl = urljoin
    globalThis.local = {
        'get': local_get, 'set': local_set, 'delete': local_delete
    }
    return globalThis
