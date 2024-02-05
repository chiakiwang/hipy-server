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


def fetch(_url, _object):
    if not isinstance(_object, dict):
        _object = ujson.loads(_object.json())

    method = (_object.get('method') or 'get').lower()
    timeout = _object.get('timeout') or 5
    body = _object.get('body') or ''
    data = _object.get('data') or {}
    if body and not data:
        for p in body.split('&'):
            k, v = p.split('=')
            data[k] = v
    headers = _object.get('headers')
    withHeaders = bool(_object.get('withHeaders') or False)
    r = None
    if method == 'get':
        r = requests.get(_url, headers=headers, params=data, timeout=timeout, verify=False)
        r.encoding = r.apparent_encoding
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
            r = _request(_url, headers=headers, data=data, timeout=timeout, verify=False)
            r.encoding = r.apparent_encoding

    if withHeaders:
        return ujson.dumps({'body': r.text if r else '', 'headers': r.headers if r else {}})
    else:
        return r.text if r else ''


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
