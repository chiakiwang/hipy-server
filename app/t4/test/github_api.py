#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : github_api.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2024/2/18
import re

import requests
import ujson

HOST = "api.github.com"
basicUrl = "https://" + HOST
# proxy = "https://gh-proxy.com/"
proxy = "https://ghproxy.liuzhicong.com/"


def getContents(repo, path, token):
    headers = {
        "Accept": "application/vnd.github.v3+json",
    }
    guest_token = token or ""
    if guest_token:
        headers["Authorization"] = "token " + guest_token
    res = requests.get(basicUrl + "/repos/" + repo + "/contents/" + (path or ""), headers=headers)
    res = res.json()
    return res


def get_js_files(repo='hjdhnx/dr_py', path='js', token='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'):
    files = getContents(repo, path, token)
    js_files = [file for file in files if str(file['name']).endswith('.js') and file['type'] == 'file']
    js_files = [{
        "rule": re.sub('\.js$', '', js_file['name']),
        "name": js_file['name'],
        "size": f"{round(js_file['size'] / 1024, 2)}kb",
        "url": proxy + js_file['download_url'],
    } for js_file in js_files]
    return js_files


def write_json(js_files):
    for index, js_file in enumerate(js_files):
        js_files[index]['id'] = index + 1
        js_files[index]['status'] = 1
    with open('drpy_rules.json', mode='w+', encoding='utf-8') as f:
        f.write(ujson.dumps(js_files, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    js_files = get_js_files()
    print(js_files)
    print(len(js_files))
    write_json(js_files)
