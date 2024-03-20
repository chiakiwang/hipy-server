#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : qjs_drpy.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2024/3/20

import os
import ujson
from quickjs import Context
from utils.quickjs_ctx import initContext


class Drpy:
    def __init__(self, key='drpy'):
        base_path = os.path.dirname(__file__)

        def _(p):
            return os.path.join(base_path, p)

        ctx = Context()
        initContext(ctx, url='', prefix_code='true', env={}, getParams=lambda: {}, getCryptoJS=lambda: 'true')
        with open(_('qjs_module_muban.js'), encoding='utf-8') as f:
            _qjs_module_muban = f.read()
        with open(_('qjs_module_cheerio.js'), encoding='utf-8') as f:
            _qjs_module_cheerio = f.read()
        with open(_('qjs_module_gbk.js'), encoding='utf-8') as f:
            _qjs_module_gbk = f.read()
        with open(_('qjs_module_crypto.js'), encoding='utf-8') as f:
            _qjs_module_crypto = f.read()
        with open(_('qjs_module_drpy2.js'), encoding='utf-8') as f:
            _qjs_module_drpy2 = f.read() + f'\nglobalThis.{key} = ' + '{ init, home, homeVod, category, detail, play, search, proxy, sniffer, isVideo};'
        ctx.module(_qjs_module_muban)
        ctx.module(_qjs_module_cheerio)
        ctx.module(_qjs_module_gbk)
        ctx.module(_qjs_module_crypto)
        ctx.module(_qjs_module_drpy2)
        self.ctx = ctx
        self.key = key

    def toJsObJect(self, any):
        if isinstance(any, dict) or isinstance(any, list):
            return self.ctx.parse_json(ujson.dumps(any, ensure_ascii=False))
        return any

    @staticmethod
    def toDict(_object):
        return ujson.loads(_object.json())

    def call(self, func: str, *args):
        return self.ctx.eval(f'globalThis.{self.key}.{func}')(*args)

    def init(self, extend=""):
        extend = self.toJsObJect(extend)
        self.call('init', extend)

    def homeContent(self, filter=None):
        filter = self.toJsObJect(filter)
        return self.call('home', filter)

    def homeVideoContent(self):
        return self.call('homeVod')

    def categoryContent(self, tid, pg, filter, extend):
        filter = self.toJsObJect(filter)
        extend = self.toJsObJect(extend)
        return self.call('category', tid, pg, filter, extend)

    def detailContent(self, ids):
        ids = self.toJsObJect(ids)
        return self.call('detail', ids)

    def searchContent(self, key, quick, pg=1):
        return self.call('search', key, quick, pg)

    def playerContent(self, flag, id, vipFlags):
        vipFlags = self.toJsObJect(vipFlags)
        return self.call('play', flag, id, vipFlags)


if __name__ == '__main__':
    drpy = Drpy()
    drpy.init('https://ghproxy.liuzhicong.com/https://github.com/hjdhnx/dr_py/raw/main/js/996%E5%BD%B1%E8%A7%86.js')
    print(drpy.homeContent())
    print(drpy.categoryContent(3, 1, False, {}))
    print(drpy.detailContent("3$/detail/790.html"))
    print(drpy.playerContent("索尼", "https://www.cs1369.com/play/790-1-1.html", []))
    # print(drpy.searchContent("斗罗大陆", False, 1))
