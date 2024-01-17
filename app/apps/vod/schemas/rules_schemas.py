#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : rules_schemas.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/1/16

from typing import List, Optional
from pydantic import BaseModel, Field, ValidationError, validator


class RulesSchema(BaseModel):
    status: int = 1
    active: bool = True
    ext: str = ''
