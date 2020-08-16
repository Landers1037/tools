# -*- coding: utf-8 -*-
# Time: 2020-04-01 18:25
# Author: Landers1037
# Mail: liaorenj@gmail.com

#超级工具集合

import click
from tools_cmd import blog,update,webp,img64,imgzip,test,system,send

@click.group(name="tools",invoke_without_command=True)
def tools():
    """
    整合工具
    """
    click.secho("It's Mgek Tools",fg="green")
    click.secho("type --help for more info",fg="blue")


#blog
tools.add_command(blog)
tools.add_command(update)
#webp
tools.add_command(webp)
#base64
tools.add_command(img64)
#imgzip
tools.add_command(imgzip)
#send
tools.add_command(send)
#test
tools.add_command(test)
tools.add_command(system)

if __name__ == '__main__':
    tools()