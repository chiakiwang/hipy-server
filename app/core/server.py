#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : server.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2023/12/3

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from apps import api_router, web_router
from starlette.middleware.cors import CORSMiddleware
from common.exceptions import customExceptions
from core.config import settings
from core.middleware import middleware
# from common.middleware import RequestsLoggerMiddleware
from db.cache import registerRedis
# from tasks.timer import scheduler # 这个是没固化数据库的。scheduler.start() 启动
from common.task_apscheduler import scheduler_register, scheduler  # 固化数据库,scheduler.init_scheduler() 初始化
from utils.notes import set_start_time


class InitializeApp(object):
    """
    注册App
    """

    def __new__(cls, *args, **kwargs):
        # app = FastAPI(title=settings.PROJECT_NAME)
        app = FastAPI(title=settings.PROJECT_NAME, middleware=middleware)
        # set static files
        app.mount("/media", StaticFiles(directory="media"), name="media")  # 媒体文件
        app.mount("/static", StaticFiles(directory="static"), name="static")  # 静态文件
        app.mount("/web", StaticFiles(directory="templates"), name="templates")  # 模板静态文件
        # allow cross domain
        # app.add_middleware(CORSMiddleware, allow_origins=settings.BACKEND_CORS_ORIGINS,
        #                    allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

        # set redis
        registerRedis(app)
        # set custom exceptions
        customExceptions(app)
        # set timer
        cls.event_init(app)
        # api router
        cls.register_router(app)

        # set socketio
        # app.mount('/', socket_app)

        # print all path
        # for _route in app.routes:
        #     r = _route.__dict__
        #     print(r['path'], r.get('methods', {}))
        return app

    @staticmethod
    def register_router(app: FastAPI) -> None:
        """
        注册路由
        :param app:
        :return:
        """
        # 项目API
        app.include_router(api_router, prefix="/api/v1")
        # 网页API
        app.include_router(web_router, prefix="")

        # app.middleware("http")(RequestsLoggerMiddleware())  # http请求请求记录中间件  不需要可以注释掉，使用了可能会影响一点请求速度

    @staticmethod
    def event_init(app: FastAPI) -> None:
        """
        事件初始化
        :param app:
        :return:
        """

        @app.on_event("startup")
        async def startup():
            set_start_time()  # 写入程序启动时间

            # scheduler.start()  # 定时任务
            # 初始化 apscheduler
            # scheduler.init_scheduler()  # noqa 去掉不合理提示
            scheduler_register()

        @app.on_event('shutdown')
        async def shutdown():
            """
            关闭
            :return:
            """
            # await mysql.close_mysql()
            scheduler.shutdown()
