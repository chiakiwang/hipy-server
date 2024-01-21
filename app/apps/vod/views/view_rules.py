#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : view_rules.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/1/14

import os
from fastapi import APIRouter, Depends, Query, File, UploadFile, Request
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc, func

from core.config import settings
from core.logger import logger
from ...permission.models import Users

from common import deps, error_code
from ..schemas import rules_schemas
from ..curd.curd_rules import curd_vod_rules as curd
from apps.system.curd.curd_dict_data import curd_dict_data
from ..models.vod_rules import VodRules

from common.resp import respSuccessJson, respErrorJson
from common.schemas import StatusSchema, ActiveSchema

from pathlib import Path

router = APIRouter()

access_name = 'vod:rules'
api_url = '/rules'


@router.get(api_url + '/list', summary="查询源列表")
async def searchRecords(*,
                        db: Session = Depends(deps.get_db),
                        status: int = Query(None),
                        name: str = Query(None),
                        group: str = Query(None),
                        file_type: str = Query(None),
                        order_by: str = Query(None),
                        is_desc: bool = Query(None),
                        page: int = Query(1, gt=0),
                        page_size: int = Query(20, gt=0),
                        ):
    order_bys = [desc(VodRules.order_num)] if is_desc else [asc(VodRules.order_num)]
    if order_by:
        if order_by == 'created_ts':
            order_bys += [desc(VodRules.created_time)] if is_desc else [asc(VodRules.created_time)]
        elif order_by == 'modified_ts':
            order_bys += [desc(VodRules.modified_time)] if is_desc else [asc(VodRules.modified_time)]
        elif order_by == 'name':
            order_bys += [desc(VodRules.name)] if is_desc else [asc(VodRules.name)]
        elif order_by == 'id':
            order_bys = [desc(VodRules.id)] if is_desc else [asc(VodRules.id)]
        elif order_by == 'order_num':
            order_bys = order_bys

    res = curd.search(db, status=status, name=name, group=group, file_type=file_type, page=page,
                      page_size=page_size, order_bys=order_bys)
    return respSuccessJson(res)


@router.get(api_url + '/{_id}', summary="查询源详细")
async def getRecord(*,
                    db: Session = Depends(deps.get_db),
                    _id: int = Query(..., title="源id"),
                    ):
    return respSuccessJson(curd.get(db, _id=_id))


@router.get(api_url + '/raw/{_id}', summary="获取源文件直链")
async def getRecordRawLink(*,
                           db: Session = Depends(deps.get_db),
                           u: Users = Depends(deps.user_perm([f"{access_name}:put"])),
                           request: Request,
                           _id: int = Query(..., title="源id"),
                           ):
    host = str(request.base_url)
    rule_data = curd.get(db, _id=_id, to_dict=False)
    groups = {}
    group_dict = curd_dict_data.getByType(db, _type='vod_rule_group')
    group_details = group_dict.get('details')
    for li in group_details:
        groups[li['label']] = li['value']
    if rule_data.group in groups.values():
        group = ''
        for key, value in groups.items():
            if value == rule_data.group:
                group = key
                break

        file_url = f'{host}files/{group}/{rule_data.name}{rule_data.file_type}'
        editable = rule_data.file_type in ['.py', '.json', '.js', '.txt', '.m3u', '.m3u8']
        return respSuccessJson({'url': file_url, 'editable': editable})
    else:
        return respErrorJson(error_code.ERROR_INTERNAL.set_msg(f"系统字典不存在值为{rule_data.group}的内容"))


@router.put(api_url + "/{_id}", summary="修改源")
async def setRecord(*,
                    db: Session = Depends(deps.get_db),
                    u: Users = Depends(deps.user_perm([f"{access_name}:put"])),
                    _id: int,
                    obj: rules_schemas.RulesSchema,
                    ):
    curd.update(db, _id=_id, obj_in=obj, modifier_id=u['id'])
    return respSuccessJson()


@router.put(api_url + '/raw/{_id}', summary="修改源文件文本")
async def setRecordRawContent(*,
                              db: Session = Depends(deps.get_db),
                              u: Users = Depends(deps.user_perm([f"{access_name}:put"])),
                              _id: int,
                              obj: rules_schemas.RulesContentSchema,
                              ):
    rule_data = curd.get(db, _id=_id, to_dict=False)
    rule_path = rule_data.path
    is_exist = rule_data.is_exist
    logger.info(f'rule_path:{rule_path}, is_exist:{is_exist}')
    obj_in = {}
    msg = '修改成功'
    if os.path.exists(rule_path):
        with open(rule_path, mode='w+', encoding='utf-8') as f:
            f.write(obj.content)
    else:
        if is_exist:
            obj_in.update({'is_exist': False})
            msg = '修改失败,待修改的文件路径不存在'
    curd.update(db, _id=_id, obj_in=obj_in, modifier_id=u['id'])
    return respSuccessJson(msg=msg)


@router.post(api_url + "/file/uploadData", summary="上传源")
async def uploadData(*,
                     u: Users = Depends(deps.user_perm([f"{access_name}:post"])),
                     db: Session = Depends(deps.get_db),
                     updateSupport: bool = Query(...),
                     group: str = Query(...),
                     files: List[UploadFile] = File(...)):
    logger.info(f'updateSupport:{updateSupport},group:{group}')
    # 获取项目根目录
    project_dir = os.getcwd()
    groups = {}
    group_dict = curd_dict_data.getByType(db, _type='vod_rule_group')
    group_details = group_dict.get('details')
    for li in group_details:
        groups[li['label']] = li['value']
    logger.info(groups)
    skip_files = []
    # 判断分组在系统字典里才进行上传操作
    if group in groups.values():
        files_data = []
        spiders_dir = os.path.join(project_dir, group)
        os.makedirs(spiders_dir, exist_ok=True)
        count = 0
        for i in files:
            fpath = os.path.join(spiders_dir, i.filename)
            fpath = Path(fpath).as_posix()
            # 如果已存在并不支持覆盖，就跳过文件
            if os.path.exists(fpath) and not updateSupport:
                skip_files.append(i.filename)
                continue
            # 不存在或者支持覆盖，构造数据
            name = os.path.basename(fpath)
            base_name, extension = os.path.splitext(name)
            files_data.append({
                'name': base_name,
                'group': group,
                'path': fpath,
                'is_exist': True,
                'file_type': extension,
            })

            # 写入本地文件
            file_content = await i.read()
            with open(fpath, 'wb') as f:
                f.write(file_content)
            count += 1

        for file_info in files_data:
            record = curd.getByName(db, file_info['name'], file_info['file_type'], file_info['group'])
            if record:
                curd.update(db, _id=record.id, obj_in=file_info, modifier_id=u['id'])
            else:
                file_info.update({
                    'order_num': 0,
                    'ext': '',
                    'status': 1,
                    'active': True,
                })
                max_order_num = curd.get_max_order_num(db)
                file_info.update({'order_num': max_order_num + 1})
                record = curd.create(db, obj_in=file_info, creator_id=u['id'])
            logger.info(f'record: id:{record.id} name:{record.name}{record.file_type}')

        return respSuccessJson(data={'path': spiders_dir, 'skip_files': skip_files},
                               msg=f'成功上传{count}个文件,跳过{len(skip_files)}个文件')

    else:
        return respErrorJson(error_code.ERROR_PARAMETER_ERROR.set_msg(f'上传失败:未知的group:{group}'))


@router.post(api_url + "/refresh", summary="刷新源")
async def refreshRules(*,
                       db: Session = Depends(deps.get_db),
                       u: Users = Depends(deps.user_perm([f"{access_name}:post"])), ):
    # 获取项目根目录
    project_dir = os.getcwd()
    groups = {}
    group_dict = curd_dict_data.getByType(db, _type='vod_rule_group')
    group_details = group_dict.get('details')
    for li in group_details:
        groups[li['label']] = li['value']
    logger.info(groups)
    files_data = []
    spiders_dirs = []
    for key, value in groups.items():
        group_label = key
        group_value = value
        spiders_dir = os.path.join(project_dir, value)
        os.makedirs(spiders_dir, exist_ok=True)
        spiders_dirs.append(spiders_dir)
        files = os.listdir(spiders_dir)
        for file in files:
            fpath = os.path.join(spiders_dir, file)
            fpath = Path(fpath).as_posix()
            # print(fpath)
            name = os.path.basename(fpath)
            base_name, extension = os.path.splitext(name)
            if os.path.isfile(fpath):
                files_data.append({
                    'name': base_name,
                    'group': group_value,
                    'path': fpath,
                    'is_exist': True,
                    'file_type': extension,
                })
    exist_records = []
    for file_info in files_data:
        record = curd.getByName(db, file_info['name'], file_info['file_type'], file_info['group'])
        if record:
            curd.update(db, _id=record.id, obj_in=file_info, modifier_id=u['id'])
        else:
            file_info.update({
                'order_num': 0,
                'ext': '',
                'status': 1,
                'active': True,
            })
            max_order_num = curd.get_max_order_num(db)
            file_info.update({'order_num': max_order_num + 1})
            record = curd.create(db, obj_in=file_info, creator_id=u['id'])
        exist_records.append(record.id)
        logger.info(f'record: id:{record.id} name:{record.name}{record.file_type}')

    records = curd.set_exist_by_ids(db, _ids=exist_records)
    logger.info(files_data)
    logger.info(f'将{len(records)}条记录设置为不存在')
    return respSuccessJson(data={'spiders_dirs': spiders_dirs}, msg='刷新成功')


@router.put(api_url + "/{_id}/active", summary="修改源是否显示")
async def setActive(*,
                    db: Session = Depends(deps.get_db),
                    u: Users = Depends(deps.user_perm([f"{access_name}:put"])),
                    _id: int,
                    obj: ActiveSchema
                    ):
    curd.setActive(db, _id=_id, active=obj.active, modifier_id=u['id'])
    return respSuccessJson()


@router.delete(api_url + "/clear", summary="清空源")
async def clearRecord(*,
                      db: Session = Depends(deps.get_db),
                      u: Users = Depends(deps.user_perm([f"{access_name}:delete"])),
                      ):
    curd.clear(db)
    table_name = settings.SQL_TABLE_PREFIX + 'vod_rules'
    sql = ''
    if 'mysql' in settings.SQLALCHEMY_ENGINE:
        sql = f"ALTER TABLE {table_name} AUTO_INCREMENT = 1"
    elif 'postgresql' in settings.SQLALCHEMY_ENGINE:
        sql = f"ALTER SEQUENCE {table_name}_id_seq RESTART WITH 1;"
        # sql = f"select setval('{table_name}_id_seq', '1') from {table_name};"
    if sql:
        logger.info(f'执行重置索引的SQL:{sql}')
        db.execute(sql)
        db.commit()
        db.close()
    return respSuccessJson()


@router.delete(api_url + "/{_ids}", summary="删除源")
async def delRecord(*,
                    db: Session = Depends(deps.get_db),
                    u: Users = Depends(deps.user_perm([f"{access_name}:delete"])),
                    _ids: str,
                    with_file: bool = Query(False),
                    ):
    logger.info(f'with_file:{with_file}')
    _ids = list(map(lambda x: int(x), _ids.split(',')))
    paths = curd.get_path_by_ids(db=db, _ids=_ids)
    # print(paths)

    resp_data = {}
    resp_msg = f'删除完成,共计{len(paths)}条数据'
    if with_file:
        skip_lists = []
        del_lists = []
        white_paths = ['两个BT', '哔滴影视', '新浪资源', '樱花动漫',
                       'base_java_loader', 'base_spider', 'cntv央视',
                       'test_1']
        for fpath in paths:
            name = os.path.basename(fpath)
            base_name, extension = os.path.splitext(name)
            if '/t4/spiders/' in fpath and base_name in white_paths:
                logger.info(f'跳过删除白名单源:{fpath}')
                skip_lists.append(fpath)
                continue
            if os.path.exists(fpath):
                os.remove(fpath)
                del_lists.append(fpath)
        resp_data = {'skip_lists': skip_lists, 'del_lists': del_lists}
        resp_msg = f'本次成功删除本地源文件{len(del_lists)}个，保留白名单文件{len(skip_lists)}个'

    curd.removes(db, _ids=_ids)
    return respSuccessJson(data=resp_data, msg=resp_msg)
