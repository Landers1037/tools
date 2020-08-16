# -*- coding: utf-8 -*-
# Time: 2020-08-15 15:50
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: cmd_blog_update.py
import click
from utils.db_trans import updateDB

@click.command()
@click.option("-p","--post",default=None,help="更新指定文章")
@click.option("-ps","--posts",default=False,is_flag=True,help="更新文章列表")
@click.option("-u","--uv",default=None,help="是否更新uv")
@click.option("-t","--tag",default=False,is_flag=True,help="更新标签")
def update(posts,post,uv,tag):
    """
    更新数据库文件
    """
    if post:
        updateDB(p=post)
        click.secho("done!", fg="green")
    elif posts:
        updateDB(ps=True)
        click.secho("done!", fg="green")
    elif tag:
        updateDB(t=True)
        click.secho("done!", fg="green")
    elif uv:
        updateDB(u=uv)
        click.secho("done!", fg="green")
    else:
        click.secho("need args!", fg="red")
