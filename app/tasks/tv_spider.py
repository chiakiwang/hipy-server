#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : tv_spider.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2024/2/20
# 电视直播爬虫

from utils.httpapi import getGitContents
from pathlib import Path
import requests
import os
import re


def main(task_id):
    print(f'=========task_id:{task_id}')
    proxy = 'https://ghproxy.liuzhicong.com/'
    files = getGitContents('ssili126/tv', '', '')
    txt_files = [file for file in files if str(file['name']).endswith('.txt') and file['type'] == 'file']
    txt_files = [{
        "rule": re.sub('\.txt$', '', txt_file['name']),
        "name": txt_file['name'],
        "size": f"{round(txt_file['size'] / 1024, 2)}kb",
        "url": proxy + txt_file['download_url'],
    } for txt_file in txt_files]
    contents = []
    error = []
    for txt_file in txt_files:
        url = txt_file['url']
        name = txt_file['name']
        try:
            r = requests.get(url, timeout=5)
            contents.append(r.text.strip())
        except Exception as e:
            error.append(name)
            print(f'未能成功获取{name}的文件内容:{e}')

    content = '\n'.join(contents)
    # 获取项目根目录
    BASE_DIR = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
    tv_path = os.path.join(BASE_DIR, 't4/files/txt/tv.txt')
    tv_path = Path(tv_path).as_posix()
    # print(tv_path)
    with open(tv_path, 'w+', encoding='utf-8') as f:
        f.write(content)
    items = content.split('\n')
    result = f'爬取直播文件行数:{len(items)}'
    if len(error) > 0:
        result += f',未能获取{",".join(error)}等文件内容'
    print(result)
    return result


if __name__ == '__main__':
    main('tv_spider')
