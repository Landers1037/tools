# -*- coding: utf-8 -*-
# Time: 2020-08-15 21:18
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: send.py

import click
from utils.send_file import send_file

@click.command()
@click.argument("file")
@click.argument("url")
def send(file,url):
    """
    发送云端文件 file+url
    """
    o = send_file(file,url)
    if o:
        click.secho("done!",fg="green")
    else:
        click.secho("failed",fg="red")