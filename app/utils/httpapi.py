#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : httpapi.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2023/12/9

from network.request import Request


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
