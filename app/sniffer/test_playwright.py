#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : test_playwright.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/3/24
# https://github.com/microsoft/playwright-python

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        browser = browser_type.launch(headless=True)
        page = browser.new_page()
        page.goto('https://www.baidu.com')
        page.screenshot(path=f'screenshot-{browser_type.name}.png')
        print(page.title())
        # page.goto('https://blog.csdn.net/qq_47993287/article/details/123170108')
        # page.screenshot(path=f'screenshot2-{browser_type.name}.png')
        # print(page.title())
        browser.close()
