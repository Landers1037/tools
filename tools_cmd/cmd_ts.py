# -*- coding: utf-8 -*-
# Time: 2020-08-17 19:19
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: cmd_ts.py

import click
from utils.hls import hls
@click.command()
@click.option("-n","--name",default=None,help="自定义输出名称")
def ts(name):
    """
    视频切片ts
    """
    hls(name)