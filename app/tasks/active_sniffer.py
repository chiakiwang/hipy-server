#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : active_sniffer.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2024/3/26
# 激活嗅探器引导任务 程序启动10秒后执行

from core.logger import logger
from datetime import datetime
import requests


# 这里面的定时任务第一个参数恒定为task_id，后面不定长传参

def active_sniffer_after_run(*args, **kwargs):
    msg = f'----------------task_id:active_sniffer_after_run,args:{args},kwargs:{kwargs}----------------'
    # msg = f'----------------args:{args},kwargs:{kwargs}----------------'
    # print(msg)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"active_sniffer.py执行一次定时任务 {now} ......")
    try:
        r = requests.get('http://localhost:5707/sniffer?active=1', timeout=2)
        msg += r.text
    except Exception as e:
        msg += f'激活嗅探器发生错误:{e}'

    return msg
