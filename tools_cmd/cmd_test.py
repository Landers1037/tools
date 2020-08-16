# -*- coding: utf-8 -*-
# Time: 2020-08-15 15:33
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: test.py
import click
import platform,sys,os

@click.command("test")
def test():
    """
    路径测试
    """
    path = os.getcwd()
    click.secho("当前路径:"+path,fg="green")

@click.command()
def system():
    """
    平台测试
    """
    p = platform.platform()
    s = sys.version
    click.secho("Your system:"+p,fg="green")
    click.secho("Python version:"+s,fg="green")