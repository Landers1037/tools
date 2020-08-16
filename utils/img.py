# -*- coding: utf-8 -*-
# Time: 2020-02-22 19:38
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: img.py

#webp转换工具,添加水印
import os,base64,click
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def transfer2webp(keep=None,water=None):
    path = os.getcwd()
    filelist = os.listdir(path)
    if not keep:
        #run normal mode
        for f in filelist:
            if len(f.split("."))>1 and check(f):
                save(f,True,water)

    else:
        for f in filelist:
            if len(f.split(".")) > 1 and check(f):
                save(f, False,water)


def save(file,flag,water):
    try:
        outname = file.split(".")[0] + ".webp"
        im = Image.open(file)
        if water:
            #添加水印
            sizex,sizey = im.size
            size = int(sizey/35)
            if size  < 15:
                size = 15
            font = ImageFont.truetype("‪C:\Windows\Fonts\Monaco.ttf",size=size)
            draw = ImageDraw.Draw(im)
            draw.text((4,4),"@Landers1037",font=font,fill="#888888")
            im.save(outname, "WEBP")
            if flag:
                os.remove(file)
            else:
                pass
        else:
            im.save(outname, "WEBP")
            if flag:
                os.remove(file)
            else:
                pass

    except Exception as e:
        print(e.args)
        click.secho("保存文件出错",fg="red")


def transfer2base64(file=None):
    if file:
        with open(file,"rb")as f:
            img = f.read()
            img64 = str(base64.b64encode(img),encoding='utf-8')
            click.secho(img64, fg="yellow")
    else:
        file_path = os.getcwd()
        all = os.listdir(file_path)
        for i in all:
            if check(i):
                with open(i, "rb")as f:
                    img = f.read()
                    img64 = str(base64.b64encode(img), encoding='utf-8')
                    click.secho(img64, fg="yellow")

def image_zip(quality):
    file_list = os.listdir(os.getcwd())
    for name in file_list:
        if check(name):
            try:
                im = Image.open(name)
                #保存到新的文件夹里
                opt = os.path.join(os.getcwd(),name)
                im.save(opt,quality=int(quality))
            except:
                click.secho("保存文件出错", fg="red")

def check(file):
    try:
        if file.split(".")[1].lower() in ["png","jpg","jpeg","bmp","webp"]:
            return True
        else:
            return False
    except:
        return False