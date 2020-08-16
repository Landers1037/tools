# -*- coding: utf-8 -*-
# Time: 2020-08-15 17:41
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: cmd_imgzip.py
import click
from utils.img import image_zip

@click.command()
@click.option("-q","--quality",default=80,help="默认分辨率调整")
def imgzip(quality):
    """
    图片压缩质量，删除原图
    """
    image_zip(quality)
    click.secho("done!",fg="green")