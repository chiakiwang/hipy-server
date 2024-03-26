#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : snif.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2024/3/26
# desc 利用playwright实现的简易播放地址嗅探器
# webdriver_manager 各个浏览器使用案例 https://blog.csdn.net/caixiangting/article/details/132049306

from urllib.parse import urlparse
from time import time
import re
# import requests
from playwright.sync_api import sync_playwright

# 储存驱动器列表,给接口缓存用
browser_drivers = []
# 全部毫秒为单位不需要转换
class SnifferPro:
    # 正则嗅探匹配表达式
    urlRegex: str = 'http((?!http).){12,}?\\.(m3u8|mp4|flv|avi|mkv|rm|wmv|mpg|m4a|mp3)\\?.*|http((?!http).){12,}\\.(m3u8|mp4|flv|avi|mkv|rm|wmv|mpg|m4a|mp3)|http((?!http).)*?video/tos*'
    urlNoHead: str = 'http((?!http).){12,}?(ac=dm&url=)'
    # 每次嗅探间隔毫秒
    delta: int = 250
    playwright = None
    browser = None
    main_page = None
    context = None
    requests = None
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    print = lambda *args:None

    def __init__(self,
                 driver_path=None,
                 _type=0,
                 wait=5,
                 head_timeout=200,
                 timeout=15000, user_agent=None, custom_regex=None, headless=False,debug=True):
        """
        初始化
        @param driver_path: 驱动器路径
        @param _type: 使用的浏览器 0:谷歌 1:edge
        @param wait:默认等待页面时间
        @param head_timeout:head请求超时
        @param timeout:嗅探超时
        @param user_agent:请求头
        @param custom_regex: 自定义嗅探正则
        """

        self.wait = wait
        self.timeout = timeout
        self.head_timeout = head_timeout
        self.driver_path = driver_path
        self._type = _type
        self.custom_regex = custom_regex
        self.headless = headless
        self.browser = self.init_browser()
        if debug:
            self.print = print

    def init_browser(self):
        """
        初始化驱动程序
        @return:
        """
        self.playwright = sync_playwright().start()  # 用这句开头
        browser = self.playwright.chromium.launch(channel="chrome", headless=self.headless)
        # browser = self.playwright.chromium.launch(headless=self.headless)
        iphone = self.playwright.devices["iPhone 6"]
        context = browser.new_context(**iphone)
        self.main_page = context.new_page()
        self.requests = context.request

        return browser

    def setCookie(self, _dict):
        """
        设置cookie。可以在嗅探前或者获取源码前设置
        @param _dict:
        @return:
        """
        self.browser.add_cookie(_dict)

    @staticmethod
    def _route_interceptor(route):
        """
        全局路由拦截器,禁止加载某些资源
        @param route:
        @return:
        """
        excluded_resource_types = ["stylesheet", "image", "font"]
        # excluded_resource_types = ["image"]
        # excluded_resource_types = []
        if route.request.resource_type in excluded_resource_types:
            # print('禁止加载资源:', excluded_resource_types, route.request.url, route.request.resource_type)
            route.abort()
        else:
            route.continue_()

    @staticmethod
    def _on_dialog(dialog):
        """
        全局弹窗拦截器
        @param dialog:
        @return:
        """
        print('on_dialog:', dialog)
        dialog.accept()

    @staticmethod
    def _on_pageerror(error):
        """
        全局页面请求错误拦截器
        @param error:
        @return:
        """
        print('on_pageerror:', error)

    def _get_page(self, headers=None):
        page = self.browser.new_page()
        page.add_init_script(path='./stealth.min.js')
        page.set_default_navigation_timeout(self.timeout)
        page.set_default_timeout(self.timeout)
        if headers is not None:
            page.set_extra_http_headers(headers=headers)
        else:
            page.set_extra_http_headers(headers={'user-agent': self.user_agent})

        page.route(re.compile(r"\.(png|jpg|jpeg|css|ttf)$"), self._route_interceptor)
        page.on("dialog", self._on_dialog)
        page.on("pageerror", self._on_pageerror)

        # page.set_viewport_size({"width": 360, "height": 540})
        return page

    def fetCodeByWebView(self, url, headers=None):
        """
        利用webview请求得到渲染完成后的源码
        @param url: 待获取源码的url
        @return:
        """
        page = self._get_page(headers)
        content = ''
        url = ''
        try:
            page.goto(url)
        except Exception as e:
            print('发生了错误:',e)
        else:
            page.wait_for_load_state('load')
            content = page.content()
            url = page.url

        print('成功关闭page')
        page.close()
        return {'content': content, 'headers': {'location': url}}

    def snifferMediaUrl(self, playUrl, mode=0, custom_regex=None):
        """
        输入播放地址，返回嗅探到的真实视频链接
        @param playUrl: 播放网页地址
        @param mode: 模式:0 嗅探到一个就返回 1:在10秒内嗅探所有的返回列表
        @param custom_regex: 自定义嗅探正则
        @return:
        """
        if custom_regex is None:
            custom_regex = self.custom_regex
        realUrl = ''
        realUrls = []
        realHeaders = {}
        headUrls = []
        t1 = time()

        page = self._get_page()

        def _on_request(request):
            nonlocal realUrl, realHeaders
            if realUrl:
                return True
            url = request.url
            method = request.method
            headers = request.headers
            resource_type = request.resource_type
            print('on_request:', url, ' method:', method, ' resource_type:', resource_type)
            if custom_regex and re.search(custom_regex, url, re.M | re.I):
                # print(message)
                realUrl = url
                realHeaders = headers
                print('on_request通过custom_regex嗅探到真实地址:', realUrl)
                return True

            if re.search(self.urlRegex, url, re.M | re.I):
                if url.find('url=http') < 0 and url.find('v=http') < 0 and url.find('.css') < 0 and url.find(
                        '.html') < 0:
                    realUrl = url
                    realHeaders = headers
                    print('on_request通过默认正则已嗅探到真实地址:', realUrl)
                    return True
            elif str(method).lower() == 'get' and str(url).startswith('http') and url != playUrl:
                parsed_url = urlparse(url)
                path = parsed_url.path
                filename = str(path.split('/')[-1])
                # 链接不含.并且正则匹配不在不head列表  或者 链接有.但是.后面没内容，也算空后缀
                if (filename and '.' not in filename and not re.search(self.urlNoHead, url, re.M | re.I)) or (
                        '.' in filename and len(filename) > 1 and not filename.split('.')[1]):
                    # 如果链接没有进行过head请求。防止多次嗅探的时候重复去head请求
                    # print('准备发起head请求:', url, headers)
                    print('准备发起head请求:', url)
                    if url not in headUrls:
                        try:
                            # print('head url:',url,'headers:',headers)
                            # r = requests.head(url=url, headers=headers, timeout=head_timeout)
                            r = self.requests.head(url=url, timeout=self.head_timeout)
                            # print('head r:',r)
                            rheaders = r.headers
                            print('rheaders:', rheaders)
                            if rheaders.get('content-type') and rheaders[
                                'content-type'] == 'application/octet-stream' and '.m3u8' in rheaders[
                                'content-disposition']:
                                realUrl = url
                                realHeaders = headers
                                print('on_request通过head请求嗅探到真实地址:', realUrl)

                                return True
                        except Exception as e:
                            print(f'head请求访问: {url} 发生了错误:{e}')

                        headUrls.append(url)



        page.on('request', _on_request)
        cost = 0
        num = 0
        try:
            page.goto(playUrl)
        except Exception as e:
            print('嗅探发生错误:',e)
            return {'url': realUrl, 'headers': {}, 'from': playUrl, 'cost': cost, 'code': 404,
                    'msg': '嗅探失败'}
        # print(page.content())

        # page.locator('#video').wait_for()
        # page.wait_for_selector('video')

        # with page.expect_request(
        #         lambda request: _get_media(request)) as second:
        #     print('expect_request已嗅探到真实地址:',second.value.url)
        #     realUrl = second.value.url
        #     # page.get_by_text("trigger request").click()
        # second_request = second.value
        # print(second_request)

        # page.wait_for_selector('video')
        # videoUrl = page.get_attribute('video', 'src')
        # print('videoUrl:', videoUrl)

        while cost < self.timeout and not realUrl:
            num += 1
            print(f'第{num}次嗅探')
            # sleep(round(delta / 1000, 2)) # 千万不能用sleep
            page.wait_for_timeout(self.delta)
            t2 = time()
            # cost = t2 - t1
            cost = round((t2 - t1) * 1000, 2)
            print(cost)

        # cost_str = str(round(cost * 1000, 2)) + 'ms'
        t2 = time()
        cost = round((t2 - t1) * 1000, 2)
        print(f'共计耗时{cost}毫秒')
        print('realUrl:', realUrl)
        print('realHeaders:', realHeaders)
        page.close()
        print('成功关闭page')
        response_headers = {}
        if realHeaders.get('referer'):
            response_headers['referer'] = realHeaders['referer']
        if realHeaders.get('user-agent'):
            response_headers['user-agent'] = realHeaders['user-agent']
        if mode == 0 and realUrl:
            return {'url': realUrl, 'headers': response_headers, 'from': playUrl, 'cost': cost, 'code': 200,
                    'msg': '嗅探成功'}
        elif mode == 1 and realUrls:
            return {'urls': realUrls, 'code': 200, 'from': playUrl, 'cost': cost, 'msg': '嗅探成功'}
        else:
            return {'url': realUrl, 'headers': response_headers, 'from': playUrl, 'cost': cost, 'code': 404,
                    'msg': '嗅探失败'}

    def close(self):
        """
        用完记得关闭驱动器
        @return:
        """
        self.main_page.close()
        self.browser.close()
        self.playwright.stop()


def main_test():
    t1 = time()
    # url = 'https://www.cs1369.com/play/2-1-94.html'
    # url = 'https://v.qq.com/x/page/i3038urj2mt.html'
    url = 'http://www.mgtv.com/v/1/290346/f/3664551.html'
    browser = SnifferPro(driver_path=None)
    ret = browser.fetCodeByWebView('https://www.freeok.pro/xplay/63170-8-12.html')
    print(ret)
    # browser.driver.get('https://www.baidu.com')
    # ret = browser.snifferMediaUrl(url)
    # # ret = browser.snifferMediaUrl('https://www.freeok.pro/xplay/63170-8-12.html')
    # print(ret)
    # ret = browser.snifferMediaUrl('http://www.mgtv.com/v/1/290346/f/3664551.html')
    # ret = browser.snifferMediaUrl('https://www.cs1369.com/play/2-1-94.html')
    # ret = browser.snifferMediaUrl('https://v.qq.com/x/page/i3038urj2mt.html')
    # print(ret)
    # ret = browser.snifferMediaUrl('https://jx.jsonplayer.com/player/?url=https://m.iqiyi.com/v_1pj3ayb1n70.html')
    # print(ret)
    ret = browser.snifferMediaUrl('https://jx.yangtu.top/?url=https://m.iqiyi.com/v_1pj3ayb1n70.html',
                                  custom_regex='http((?!http).){12,}?(download4|pcDownloadFile)')
    print(ret)

    browser.close()
    t2 = time()
    print(f'共计耗时:{round(t2 - t1, 2)}s')


def demo_test():
    t1 = time()
    browser = SnifferPro()
    ret = browser.fetCodeByWebView('https://www.ip.cn/api/index?ip&type=0')
    print(ret)
    browser.close()
    t2 = time()
    print(f'共计耗时:{round(t2 - t1, 2)}s')


if __name__ == '__main__':
    # demo_test()
    main_test()
