#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : httpapi.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2023/12/9

from network.request import Request
from t4.base.htmlParser import jsoup
import ujson


def get_location_by_ip(ipaddr):
    login_location = ''
    try:
        ip_url = f'https://qifu-api.baidubce.com/ip/geo/v1/district?ip={ipaddr}'
        request = Request(method="GET", url=ip_url, agent=False, follow_redirects=True, timeout=0.5)
        # 同步
        r = request.request()
        resp = r.json()
        if resp.get('msg') == '查询成功':
            d = resp['data']
            prov = d['prov']
            city = d['city']
            district = d['district']
            owner = d['owner']
            login_location = f'{prov}{city}{district}{owner}'
    except Exception as e:
        print(f'查询ip归属地发生错误:{e}')

    return login_location


def getHotSuggest1(url='http://4g.v.sogou.com/hotsugg', size=0):
    headers = {
        'Referer': 'https://gitcode.net/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    }
    jsp = jsoup(url)
    pdfh = jsp.pdfh
    pdfa = jsp.pdfa
    pd = jsp.pd
    try:
        request = Request(method="GET", url=url, headers=headers, agent=False, follow_redirects=True, timeout=2)
        r = request.request()
        html = r.text
        data = pdfa(html, 'ul.hot-list&&li')
        suggs = [{'title': pdfh(dt, 'a&&Text'), 'url': pd(dt, 'a&&href')} for dt in data]
        return suggs
    except:
        return []


def getHotSuggest2(url='https://pbaccess.video.qq.com/trpc.videosearch.hot_rank.HotRankServantHttp/HotRankHttp',
                   size=0):
    size = int(size) if size else 50
    pdata = ujson.dumps({"pageNum": 0, "pageSize": size})
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
        'content-type': 'application/json'}
    try:
        request = Request(method="POST", url=url, data=pdata, headers=headers, agent=False, follow_redirects=True,
                          timeout=2)
        r = request.request()
        html = r.json()
        data = html['data']['navItemList'][0]['hotRankResult']['rankItemList']
        suggs = [{'title': dt['title'], 'url': dt['url']} for dt in data]
        return suggs
    except:
        return []


def getHotSuggest(s_from, size):
    if s_from == 'sougou':
        return getHotSuggest1(size=size)
    else:
        return getHotSuggest2(size=size)
