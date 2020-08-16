# -*- coding: utf-8 -*-
# Time: 2020-08-15 16:32
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: cmd_webp.py
import click
from utils.img import *

@click.command()
@click.option("-k","--keep",is_flag=True,default=False,help="保存原图")
@click.option("-w","--water",is_flag=True,default=False,help="开启水印")
def webp(keep,water):
    """
    webp转换
    """
    if not keep:
        if water:
            transfer2webp(water=True)
        else:
            transfer2webp(water=False)
    else:
        if water:
            transfer2webp(keep=True,water=True)
        else:
            transfer2webp(keep=True,water=False)
