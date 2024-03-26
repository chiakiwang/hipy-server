#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : snifferPro.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/3/26
# chromium 最快最好用
import re
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright
from time import time,sleep

t1 = time()
timeout = 10000
delta = 250
head_timeout = 200
with sync_playwright() as p:
    # for browser_type in [p.chromium, p.firefox, p.webkit]:
    for browser_type in [p.chromium]:
        browser = browser_type.launch(headless=True)
        context = browser.new_context()
        requests = context.request
        # page = context.new_page()
        page = browser.new_page()
        page.set_default_navigation_timeout(timeout)
        page.set_default_timeout(timeout)

        #
        # def handler():
        #     print('出现了确认您是真人')
        #     # page.get_by_role("button", name="No thanks").click()
        #
        #
        # page.set_extra_http_headers(headers={
        #     "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"})
        #
        # page.add_locator_handler(page.locator('.ctp-label',has_text="真人"), handler)
        # page.goto('https://www.freeok.pro/xplay/63170-8-12.html')
        # page.expect_request_finished()
        # # page.locator('.ctp-label').wait_for()
        # # page.wait_for_selector('.ctp-label')
        # print('卡死')
        #
        # # page.wait_for_timeout(3000)
        # print(page.content())
        # html = page.content()
        # while '是真人' in html:
        #     page.wait_for_timeout(1000)
        #     html = page.content()
        #     print(html)
        #     if '请完成以下操作，验证您是真人' in html:
        #         break
        # # print(page.content())
        # print('点击确认框准备结束')
        # # page.locator('input[type=checkbox]')
        # # page.wait_for_selector('input[type=checkbox]').check()
        # page.get_by_role("checkbox").check()
        # page.get_by_role("textbox").click()
        # exit()




        urlRegex: str = 'http((?!http).){12,}?\\.(m3u8|mp4|flv|avi|mkv|rm|wmv|mpg|m4a|mp3)\\?.*|http((?!http).){12,}\\.(m3u8|mp4|flv|avi|mkv|rm|wmv|mpg|m4a|mp3)|http((?!http).)*?video/tos*'
        urlNoHead: str = 'http((?!http).){12,}?(ac=dm&url=)'
        realUrl = ''
        headUrls = []

        def on_request(request):
            global realUrl
            url = request.url
            method = request.method
            headers = request.headers
            resource_type = request.resource_type
            print('on_request:', url, ' method:', method, ' resource_type:', resource_type)
            if re.search(urlRegex, url, re.M | re.I):
                if url.find('url=http') < 0 and url.find('v=http') < 0 and url.find('.css') < 0 and url.find(
                        '.html') < 0:
                    realUrl = url
                    print('on_request已嗅探到真实地址:', realUrl)
                    return True
            elif str(method).lower() == 'get' and str(url).startswith('http') and url != playUrl:
                parsed_url = urlparse(url)
                path = parsed_url.path
                filename = str(path.split('/')[-1])
                # 链接不含.并且正则匹配不在不head列表  或者 链接有.但是.后面没内容，也算空后缀
                if (filename and '.' not in filename and not re.search(urlNoHead, url, re.M | re.I)) or (
                        '.' in filename and len(filename) > 1 and not filename.split('.')[1]):
                    # 如果链接没有进行过head请求。防止多次嗅探的时候重复去head请求
                    print('准备发起head请求:', url, headers)
                    if url not in headUrls:
                        try:
                            print('head url:',url,'headers:',headers)
                            # r = requests.head(url=url, headers=headers, timeout=head_timeout)
                            r = requests.head(url=url, timeout=head_timeout)
                            print('head r:',r)
                            rheaders = r.headers
                            print('rheaders:',rheaders)
                            if rheaders.get('content-type') and rheaders[
                                'content-type'] == 'application/octet-stream' and '.m3u8' in rheaders[
                                'content-disposition']:
                                realUrl = url
                                print('on_request嗅探到真实地址:',realUrl)

                                return True
                        except Exception as e:
                            print(f'head请求访问: {url} 发生了错误:{e}')

                        headUrls.append(url)

        def on_pageerror(exc):
            print('on_pageerror:',exc)

        def on_dialog(dialog):
            print('on_dialog:',on_dialog)
            dialog.accept()

        def handle_media(route):
            global realUrl
            print('handle_media已嗅探到真实地址::',route.request.url)
            realUrl = route.request.url

        def handler():
            print('视频准备就绪')

        def handler1():
            print('获取到定位器')

        # page.add_locator_handler(page.get_by_text("视频已准备就绪"), handler)
        # page.add_locator_handler(page.locator("video#video"), handler1)

        # page.route(re.compile(r"\.(m3u8)"), handle_media)
        page.on('request',on_request)
        page.on("pageerror", on_pageerror)


        def _router(route):
            excluded_resource_types = ["stylesheet", "image","font"]
            if route.request.resource_type in excluded_resource_types:
                print('禁止加载资源:', excluded_resource_types, route.request.url, route.request.resource_type)
                route.abort()
            else:
                route.continue_()

        # page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
        page.route(re.compile(r"\.(png|jpg|jpeg|css|ttf)$"), _router)
        # page.route(re.compile(r"\.(png|jpg|jpeg)$"), lambda route: route.continue_())
        # page.route(re.compile(r"\.(css)$"), lambda route: route.abort())

        page.set_viewport_size({"width": 360, "height": 540})
        page.on("dialog", on_dialog)
        page.set_extra_http_headers(headers={"user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"})
        playUrl='https://jx.jsonplayer.com/player/?url=https://m.iqiyi.com/v_1pj3ayb1n70.html'
        playUrl = 'https://jx.yangtu.top/?url=https://m.iqiyi.com/v_1pj3ayb1n70.html'
        page.goto(playUrl)
        # print(page.content())
        cost = 0
        num = 0
        # page.locator('#video').wait_for()
        # page.wait_for_selector('video')
        def _get_media(request):
            global realUrl
            url = request.url
            method = request.method
            headers = request.headers
            resource_type = request.resource_type
            print('_get_media_url:',url,' method:',method,' resource_type:',resource_type)
            if re.search(urlRegex, url, re.M | re.I):
                if url.find('url=http') < 0 and url.find('v=http') < 0 and url.find('.css') < 0 and url.find(
                        '.html') < 0:
                    realUrl = url
                    print('_get_media已嗅探到真实地址:', realUrl)
                    return True
            elif str(method).lower() == 'get' and str(url).startswith('http') and url != playUrl:
                parsed_url = urlparse(url)
                path = parsed_url.path
                filename = str(path.split('/')[-1])
                # 链接不含.并且正则匹配不在不head列表  或者 链接有.但是.后面没内容，也算空后缀
                if (filename and '.' not in filename and not re.search(urlNoHead, url, re.M | re.I)) or (
                        '.' in filename and len(filename) > 1 and not filename.split('.')[1]):
                    # 如果链接没有进行过head请求。防止多次嗅探的时候重复去head请求
                    print('准备发起head请求:',url,headers)
                    if url not in headUrls:
                        try:
                            r = requests.head(url=url, headers=headers, timeout=head_timeout)
                            rheaders = r.headers
                            if rheaders.get('Content-Type') and rheaders[
                                'Content-Type'] == 'application/octet-stream' and '.m3u8' in rheaders[
                                'Content-Disposition']:
                                realUrl = url

                                return True
                        except Exception as e:
                            print(f'head请求访问: {url} 发生了错误:{e}')

                        headUrls.append(url)

            return False

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



        while cost < timeout and not realUrl:
            num+=1
            print(f'第{num}次嗅探')
            # sleep(round(delta / 1000, 2)) # 千万不能用sleep
            page.wait_for_timeout(delta)
            t2 = time()
            # cost = t2 - t1
            cost = round((t2 - t1) * 1000, 2)
            print(cost)

        # cost_str = str(round(cost * 1000, 2)) + 'ms'
        t2 = time()
        cost = round((t2 - t1) * 1000, 2)
        print(f'共计耗时{cost}毫秒')
        print('realUrl:',realUrl)
        page.close()
        print('成功关闭page')
        browser.close()
        print('成功关闭browser')