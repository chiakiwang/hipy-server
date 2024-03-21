#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : vod_tool.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2024/2/5

import ujson
from time import time
import base64
import requests
import warnings

# 关闭警告
warnings.filterwarnings("ignore")
requests.packages.urllib3.disable_warnings()


def base_request(_url, _object, _js_type=0):
    """
    基础网络请求封装，兼容qjs和pythonmonkey引擎二次使用
    @param _url:网页地址
    @param _object: 必要参数字典 method,timeout,body,data,headers,withHeaders 等
    @param _js_type: 0 qjs 1 pythonmonkey
    @return:
    """
    if not isinstance(_object, dict) and _js_type == 0:
        _object = ujson.loads(_object.json())
    elif _js_type == 1:
        _object = dict(_object)

    method = (_object.get('method') or 'get').lower()
    timeout = _object.get('timeout') or 5
    body = _object.get('body') or ''
    data = _object.get('data') or {}
    if body and not data:
        for p in body.split('&'):
            k, v = p.split('=')
            data[k] = v
    headers = _object.get('headers') or {}
    encoding = _object.get('encoding') or 'utf-8'
    buffer = _object.get('buffer') or 1

    # 修复pythonmonkey没有自动把 JSObjectProxy 转为python的dict导致的后续错误
    data = dict(data)
    headers = dict(headers)

    withHeaders = bool(_object.get('withHeaders') or False)
    r = None
    r_text = ''
    r_content = b''
    r_headers = {}
    if method == 'get':
        try:
            r = requests.get(_url, headers=headers, params=data, timeout=timeout, verify=False)
            # r.encoding = r.apparent_encoding
            r.encoding = encoding
            r_text = r.text
            r_content = r.content
            r_headers = dict(r.headers)
        except Exception as e:
            error = f'base_request {method} 发生了错误:{e}'
            r_headers['error'] = error
            print(error)
    else:
        _request = None
        if method == 'post':
            _request = requests.post
        elif method == 'put':
            _request = requests.put
        elif method == 'delete':
            _request = requests.delete
        elif method == 'head':
            _request = requests.head

        if _request:
            try:
                r = _request(_url, headers=headers, data=data, timeout=timeout, verify=False)
                # r.encoding = r.apparent_encoding
                r.encoding = encoding
                r_text = r.text
                r_content = r.content
                r_headers = dict(r.headers)
            except Exception as e:
                error = f'base_request {method} 发生了错误:{e}'
                r_headers['error'] = error
                print(error)
    if buffer == 2:
        r_text = base64.b64encode(r_content).decode("utf8")
    empty_result = {'content': '', 'body': '', 'headers': {}}
    if withHeaders and _js_type == 0:
        result = {'body': r_text, 'headers': r_headers} if r else empty_result
        return ujson.dumps(result)
    elif not withHeaders and _js_type == 0:
        return r_text if r else ''
    elif _js_type == 1:
        result = {'content': r_text, 'headers': r_headers} if r else empty_result
        return result
    else:
        return empty_result


def fetch(_url, _object):
    """
    qjs试用的fetch函数
    @param _url:
    @param _object:
    @return:
    """
    return base_request(_url, _object, 0)


def req(_url, _object):
    """
    tvbox注入的pythonmoneky版req函数
    @param _url:
    @param _object:
    @return:
    """
    return base_request(_url, _object, 1)


def 重定向(_url: str):
    if _url.startswith('http'):
        return f'redirect://{_url}'
    else:
        return str(_url)


def toast(_url: str):
    return f'toast://{_url}'


def image(_text: str):
    return f'image://{_text}'


def base64ToImage(_image_base64: str):
    if ',' in _image_base64:
        _image_base64 = _image_base64.split(',')[1]
    _img_data = base64.b64decode(_image_base64)
    return _img_data


def get_interval(t):
    interval = time() - t
    interval = round(interval * 1000, 2)
    return interval
