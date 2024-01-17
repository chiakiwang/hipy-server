#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : web.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2023/12/3
import os
from core.config import settings
from jinja2 import Environment, FileSystemLoader


class HtmlSender:
    ENV = Environment(loader=FileSystemLoader('./'))

    def __int__(self):
        pass

    @property
    def template_path(self) -> str:
        return self.ENV.loader

    @template_path.setter
    def template_path(self, path):
        try:
            if os.path.isdir(path):
                self.ENV = Environment(loader=FileSystemLoader(path))
            else:
                raise ValueError("template_path must dir")
        except Exception as e:
            raise ValueError("template_path must dir") from e

    def renderTemplate(self, template_name: str, data: dict = None) -> str:
        data = data or {}
        temp = self.ENV.get_template(f"{template_name}.html")
        return temp.render(**data)


htmler = HtmlSender()
htmler.template_path = settings.WEB_TEMPLATES_DIR

# print('===template_path===:', settings.WEB_TEMPLATES_DIR)
