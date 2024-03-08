#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : pm_env.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2024/2/29

from t4.base.htmlParser import jsoup
from utils.vod_tool import fetch, 重定向, toast, image
from utils.local_cache import local

def get_env():
    print(type(local.set))
    print(type(local.get))
    local_set = getattr(local, "set", None)
    print(type(local_set))
    print(type(jsoup.pdfh))
    return {
        "local":local,
        "jsoup":jsoup,
        "pdfh":jsoup.pdfh,
        "pdfa":jsoup.pdfa,
        "pd":jsoup.pd,
        "set":local.set,
        "get":local.get,
    }

exports = {
    "local": local,
    "jsoup": jsoup,
    "get_env": get_env,
    "rule":{}
}
