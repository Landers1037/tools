# -*- coding: utf-8 -*-
# Time: 2020-08-15 15:32
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: blog.py
import click,os
from utils.db_trans import *
from utils.to_json import newjson

@click.command()
@click.option("-r","--remove",is_flag=True,default=False,help="删除数据库")
@click.option("-n","--new",is_flag=True,default=False,help="新建数据库")
@click.option("-j","--json",default=None,help="json文件")
@click.option("-t","--test",default=None,help="文章测试")
def blog(remove,new,json,test):
    """
    生成/删除数据库文件
    """
    if remove:
        opt = os.path.join(os.path.expanduser("~"), 'Desktop', 'blog_opt')
        flag = os.path.exists(os.path.join(opt, "app.db"))
        if flag:
            click.secho("db file exists.It will be removed!", fg="yellow")
            os.remove(os.path.join(opt, "app.db"))
        else:
            click.secho("db file not exists!", fg="yellow")
        click.secho("done!", fg="green")

    elif new:
        newDB()
        click.secho("done!",fg="green")

    elif json:
        try:
            newjson(json)
            click.secho("done! blog.json generated", fg="yellow")
        except:
            click.secho("error!", fg="red")

    elif test:
        blog_test()
    else:
        click.secho("please type args!", fg="green")


