#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : views.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2023/12/3

from fastapi import APIRouter, Depends, Query, WebSocket, Request as Req, HTTPException
from starlette.responses import HTMLResponse, RedirectResponse
import os
from common import error_code, deps
from sqlalchemy.orm import Session
from core.config import settings
from core.logger import logger
from utils.web import htmler
from utils.cmd import update_db
from utils.httpapi import get_location_by_ip
from network.request import Request
from common.resp import respSuccessJson, respErrorJson
from .schemas import database_schemas
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
from apps.system.curd.curd_dict_data import curd_dict_data

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
    return FileResponse('static/img/favicon.svg')


@router.get('/blog', summary="博客首页")
async def blog():
    return RedirectResponse(settings.BLOG_URL)


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
    error_msg = f'group:{group},filename:{filename}'
    host = str(request.base_url)
    # logger.info(f'host:{host}')
    # 获取项目根目录
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
            raise HTTPException(status_code=404)
        else:
            if filename.endswith('.js'):
                return FileResponse(file_path, media_type='text/javascript; charset=utf-8')

            return FileResponse(file_path)

    else:
        logger.info(f'{error_msg},groups:{groups}')
        raise HTTPException(status_code=404)


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
