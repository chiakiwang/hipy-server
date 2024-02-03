#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : views.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2023/12/3
import ujson
from fastapi import APIRouter, Depends, Query, WebSocket, Request as Req, HTTPException
from starlette.responses import HTMLResponse, RedirectResponse, Response
import os
from common import error_code, deps
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc, func
from core.config import settings
from core.logger import logger
from utils.web import htmler, render_template_string, remove_comments
from utils.cmd import update_db
from utils.httpapi import get_location_by_ip, getHotSuggest
from network.request import Request
from common.resp import respSuccessJson, respErrorJson, abort
from .schemas import database_schemas
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
from apps.system.curd.curd_dict_data import curd_dict_data
from apps.vod.curd.curd_rules import curd_vod_rules
from apps.vod.curd.curd_configs import curd_vod_configs

try:
    from redis.asyncio import Redis as asyncRedis
except ImportError:
    from aioredis import Redis as asyncRedis

router = APIRouter()
# htmler2 = Jinja2Templates(directory="templates")
htmler2 = Jinja2Templates(directory=settings.WEB_TEMPLATES_DIR)

# 存储所有连接到 WebSocket 的客户端
client_websockets = []


@router.get("/doc", response_class=HTMLResponse, summary="文档首页")
async def read_root(request: Req):
    return htmler2.TemplateResponse("index.html", {"request": request})


@router.get("/", summary="网站首页")
async def web_home():
    html = htmler.renderTemplate('index')
    return HTMLResponse(html)


@router.get('/favicon.ico', summary="网站默认图标")  # 设置icon
async def favicon():
    # return RedirectResponse('/static/img/favicon.svg')
    return FileResponse('static/img/favicon.ico')


@router.get('/blog', summary="博客首页")
async def blog():
    return RedirectResponse(settings.BLOG_URL)


# @router.get('/test')
# async def api_test():
#     """
#     这个例子就是很好的测试。加了async内部的代码逻辑不能去调用自己的其他接口否则会阻塞无法获取
#     @return:
#     """
#     import requests
#     r = requests.get('http://192.168.31.49:5707/files/hipy/两个BT.json', timeout=5)
#     print(r.text)
#     return respSuccessJson(data=r.json())


@router.get("/config/{mode}", summary="自动生成tvbox-hipy配置")
async def hipy_configs(*,
                       db: Session = Depends(deps.get_db),
                       r: asyncRedis = Depends(deps.get_redis),
                       request: Req,
                       mode: int = Query(..., title="模式 0:t4 1:t3"),
                       ):
    host = str(request.base_url).rstrip('/')
    groups = {}
    group_dict = curd_dict_data.getByType(db, _type='vod_rule_group')
    group_details = group_dict.get('details')
    for li in group_details:
        groups[li['label']] = li['value']
    order_bys = [asc(curd_vod_rules.model.order_num)]
    hipy_rules = curd_vod_rules.search(db=db, status=1, group=groups['hipy'], file_type='.py', page=1, page_size=9999,
                                       order_bys=order_bys)
    drpy_rules = curd_vod_rules.search(db=db, status=1, group=groups['drpy_js'], page=1, page_size=9999,
                                       order_bys=order_bys)
    # print(hipy_rules.get('results')[0])
    hipy_rules = [{
        'name': rec['name'],
        'file_type': rec['file_type'],
        'ext': rec['ext'] or '',
        'searchable': rec['searchable'],
        'quickSearch': rec['quickSearch'],
        'filterable': rec['filterable'],
        'order_num': rec['order_num'],
    } for rec in hipy_rules.get('results') or [] if rec['active'] and rec['is_exist']]

    drpy_rules = [{
        'name': rec['name'],
        'file_type': rec['file_type'],
        'ext': rec['ext'] or '',
        'searchable': rec['searchable'],
        'quickSearch': rec['quickSearch'],
        'filterable': rec['filterable'],
        'order_num': rec['order_num'],
    } for rec in drpy_rules.get('results') or [] if rec['active'] and rec['is_exist']]

    # print(hipy_rules)
    # print(drpy_rules)
    try:
        key = 'vod_config_base'
        if r:
            vod_configs_obj = await curd_vod_configs.getByKeyWithCache(r, db, key=key)
        else:
            vod_configs_obj = curd_vod_configs.getByKey(db, key=key)

        cf_value = vod_configs_obj.get('value')
        cf_value_type = vod_configs_obj.get('value_type')
    except Exception as e:
        logger.info(f'获取vod_config_base发生错误:{e}')
        cf_value = ''
        cf_value_type = 'error'

    if cf_value_type == 'file':
        data, total, offset, limit = curd_vod_configs.get_multi(db, page=1, page_size=99,
                                                                order_bys=[asc(curd_vod_configs.model.order_num)])
        # print(data)
        config = {}
        jxs = []
        for d in data:
            if d['value_type'] == 'file':
                config[d['key']] = f"{host}/files/{d['value']}"
            else:
                config[d['key']] = d['value']

            if d['key'] == 'vod_vip_parse' and d['value_type'] == 'file':
                d_value = d['value']
                d_group = d_value.split('/')[0]
                d_file_name = '/'.join(d_value.split('/')[1:])
                resp = get_file_path(db, d_group, d_file_name)
                if isinstance(resp, list):
                    jx_file_path = resp[0]
                    # print(jx_file_path)
                    with open(jx_file_path, encoding='utf-8') as f:
                        jx_content = f.read()
                    jx_content = remove_comments(jx_content)
                    for jx in jx_content.split('\n'):
                        jx = jx.strip()
                        jx_arr = jx.split(',')
                        if len(jx_arr) > 1:
                            jx_name = jx_arr[0]
                            jx_url = jx_arr[1]
                            jx_type = jx_arr[2] if len(jx_arr) > 2 else 0
                            jx_ua = jx_arr[3] if len(jx_arr) > 3 else ''
                            jx_flag = jx_arr[4] if len(jx_arr) > 4 else ''
                            jxs.append({
                                'name': jx_name,
                                'url': jx_url,
                                'type': jx_type,
                                'ua': jx_ua,
                                'flag': jx_flag,
                            })

        group = cf_value.split('/')[0]
        file_name = '/'.join(cf_value.split('/')[1:])
        resp = get_file_path(db, group, file_name)
        if isinstance(resp, int):
            return abort(404, f'invalid value:{cf_value},file not found')
        file_path = resp[0]

        rules = hipy_rules + drpy_rules
        # 按order_num排序
        rules.sort(key=lambda x: x['order_num'])

        rules = ujson.dumps(rules, ensure_ascii=False)
        # rules里支持{{host}}渲染
        rules = render_template_string(rules, **{'host': host})
        rules = ujson.loads(rules)
        # print(rules)
        # 自定义额外sites,从用户附加里面去获取
        sites = []

        context = {'config': config, 'rules': rules,
                   'host': host, 'mode': mode, 'sites': sites,
                   'jxs': jxs, 'alists': [],
                   }
        # print(context)
        try:
            with open(file_path, encoding='utf-8') as f:
                file_content = f.read()
            render_text = render_template_string(file_content, **context)
            # 单引号替换双引号
            render_text = render_text.replace("'", '"')
            # render_dict = json.loads(render_text)
            # print(render_dict)
            # return HTMLResponse(render_text)
            # rules经过{{host}}渲染后这里不需要二次渲染
            # render_text = render_template_string(render_text, **context)
            return Response(status_code=200, media_type='text/plain', content=render_text)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"{e}")
            # raise HTTPException(status_code=500)
    else:
        return abort(404, f'invalid value_type:{cf_value_type},only file allowed')


def get_file_path(db, group, filename):
    """
    获取本地文件路径和类型
    @param db: 数据库游标
    @param group: 文件组label
    @param filename: 文件名称带后缀
    @return: 404 [file_path,media_type] [file_path]
    """
    error_msg = f'group:{group},filename:{filename}'
    project_dir = os.getcwd()
    groups = {}
    group_dict = curd_dict_data.getByType(db, _type='vod_rule_group')
    group_details = group_dict.get('details')
    for li in group_details:
        groups[li['label']] = li['value']
    # 判断分组在系统字典里才进行上传操作
    if group in groups.keys():
        folder_path = groups[group]
        folder_path = os.path.join(project_dir, folder_path)
        file_path = os.path.join(folder_path, filename)
        if not os.path.exists(file_path):
            logger.info(f'{error_msg},file_path:{file_path}')
            return 404
        else:
            if filename.endswith('.js'):
                return [file_path, 'text/javascript; charset=utf-8']

            return [file_path]

    else:
        logger.info(f'{error_msg},groups:{groups}')
        return 404


@router.get("/files/{group}/{filename:path}", summary="T4静态文件")
async def t4_files(*,
                   db: Session = Depends(deps.get_db),
                   request: Req,
                   group: str = Query(..., title="hipy源分组"),
                   filename: str = Query(..., title="hipy源文件名")):
    """
    返回静态文件链接
    @param request: Request请求
    @param group: hipy文件分组
    @param filename: 文件名
    @return:
    """
    host = str(request.base_url)
    # logger.info(f'host:{host}')
    resp = get_file_path(db, group, filename)
    if isinstance(resp, int):
        raise HTTPException(status_code=resp)

    file_path = resp[0]
    if len(resp) > 1:
        media_type = resp[1]
        return FileResponse(file_path, media_type=media_type)
    else:
        return FileResponse(file_path)


@router.get('/baidu', summary="访问百度")
async def baidu():
    # url = "https://www.iesdouyin.com/web/api/v2/user/info?sec_uid=MS4wLjABAAAAc4BIGF22ZcPBMtc73GAKSf-vEiPWKTLC3RJA423NK_E"
    url = "https://www.baidu.com"
    request = Request(method="GET", url=url, agent=False, follow_redirects=True)
    # 异步
    r = await request.fetch()
    # 同步
    # r = request.request()
    # print(r.text)
    return HTMLResponse(r.text)


@router.get('/get_ip_location/{ipaddr}', summary="获取ip归属地")
async def get_ip_location(ipaddr):
    return HTMLResponse(get_location_by_ip(ipaddr))


@router.get('/hotsugg', summary="获取热搜")
async def get_hot_search(*, request: Req, ):
    """
    默认腾讯接口，支持size=50;
    可传from=sougou但是不支持size
    from: sougou
    size: 50
    @param request:
    @return:
    """

    def getParams(key=None, value=''):
        return request.query_params.get(key) or value

    s_from = getParams('from')
    size = getParams('size')
    data = getHotSuggest(s_from, size)
    return respSuccessJson(data=data)


@router.put('/database_update', summary="数据库升级")
async def database_update(obj: database_schemas.updateSchema):
    if obj.auth_code == settings.DATABASE_UPDATE_AUTH:
        code, result = update_db()
        if code == 0:
            return respSuccessJson()
        # return respErrorJson(error=error_code.ERROR_DATABASE_CMD_ERROR)
        return respSuccessJson(data={"error": error_code.ERROR_DATABASE_CMD_ERROR.msg + " " + result})
    else:
        # return respErrorJson(error=error_code.ERROR_DATABASE_AUTH_ERROR)
        return respSuccessJson(data={"error": error_code.ERROR_DATABASE_AUTH_ERROR.msg})


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # 添加客户端到存储列表中
    client_websockets.append(websocket)

    # 发送欢迎信息给客户端
    await websocket.send_text("Welcome to the WebSocket server!")

    # 循环读取客户端发送的消息，并广播给所有客户端
    while True:
        data = await websocket.receive_text()
        for client in client_websockets:
            await client.send_text(f"User {id(websocket)} says: {data}")


# 静态页面，用于测试 WebSocket
html = """
<!DOCTYPE html>
<html>
    <head>
        <title>WebSocket Test</title>
        <script>
            var ws = new WebSocket("ws://" + window.location);
            ws.onopen = function(event) {
                console.log("WebSocket opened.");
            };

        ws.onmessage = function(event) {
            console.log(event.data);
        };

        function sendMessage() {
            var input = document.getElementById("message");
            var message = input.value;
            ws.send(message);
            input.value = "";
        }
    </script>
</head>
<body>
    <h1>WebSocket Test</h1>
    <div>
        <input type="text" id="message">
        <button onclick="sendMessage()">Send</button>
    </div>
  </body>
</html>
"""


# 返回静态页面
@router.get("/ws")
async def websocket_html():
    return HTMLResponse(html)
