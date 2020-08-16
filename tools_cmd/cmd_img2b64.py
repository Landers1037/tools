# -*- coding: utf-8 -*-
# Time: 2020-08-15 20:43
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: cmd_img2b64.py
import click
from utils.img import transfer2base64

@click.command()
@click.option("-f","--file",default=None,help="图片转base64")
def img64(file):
    """
    图片转base64
    """
    transfer2base64(file)

