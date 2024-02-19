#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : views_houses.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2024/2/19

from typing import Any, Optional, List

import ujson
from core.logger import logger
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from common import deps
from common.resp import respSuccessJson
from ..curd.curd_configs import curd_vod_configs as curd
import os
from pathlib import Path
from utils.httpapi import getGitContents, getJSFiles
from apps.permission.models import Users

router = APIRouter()

access_name = 'vod:houses'
api_url = '/houses'


@router.get(api_url + '/list', summary="查询仓库源列表")
async def searchRecords(*,
                        u: Users = Depends(deps.user_perm([f"{access_name}:get"])),
                        page: int = 1,
                        page_size: int = 20,
                        rule: str = "",
                        status: int = None
                        ):
    project_dir = os.getcwd()
    file_path = os.path.join(project_dir, 't4/files/json/drpy_rules.json')
    file_path = Path(file_path).as_posix()
    try:
        with open(file_path, encoding='utf-8') as f:
            records = ujson.loads(f.read())
    except Exception as e:
        logger.info(f'读取本地drpy仓库源文件发送了错误:{e}')
        records = []
    if records:
        if rule:
            records = [record for record in records if rule in record['rule']]
        if status is not None:
            records = [record for record in records if status == record['status']]

    total = len(records)
    start = page_size * (page - 1)
    end = page_size * page
    res = {
        'data': records[start:end], 'total': total
    }

    return respSuccessJson(res)


@router.post(api_url + "/refresh", summary="刷新配置")
def refreshRecords(*,
                   db: Session = Depends(deps.get_db),
                   u: Users = Depends(deps.user_perm([f"{access_name}:post"])), ):
    token = curd.getByKey(db, key='vod_git_token').get('value')
    proxy = curd.getByKey(db, key='vod_git_proxy').get('value')
    logger.info(f'token:{token},proxy:{proxy}')
    houses = curd.getHouses(db)
    houses = [h for h in houses if '|' in h['value']]
    records = []

    project_dir = os.getcwd()
    file_path = os.path.join(project_dir, 't4/files/json/drpy_rules.json')
    file_path = Path(file_path).as_posix()

    drpy_dir = os.path.join(project_dir, 't4/files/drpy_js/')

    _id = 1
    for house in houses:
        name = house['name']
        repo = house['value'].split('|')[0]
        path = house['value'].split('|')[1]
        js_files = getJSFiles(repo, path, token, proxy)
        for js_file in js_files:
            js_file['id'] = _id
            js_file['from'] = name
            local_file = os.path.join(drpy_dir, js_file['name'])
            if os.path.exists(local_file):
                js_file['status'] = 1
            else:
                js_file['status'] = 0
            records.append(js_file)
            _id += 1

    with open(file_path, mode='w+', encoding='utf-8') as f:
        f.write(ujson.dumps(records, ensure_ascii=False, indent=4))
    return respSuccessJson(data={}, msg='刷新成功')
