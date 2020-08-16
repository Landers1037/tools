# -*- coding: utf-8 -*-
# Time: 2020-03-12 18:36
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: new_json.py

from . import xmltodict
from urllib import parse
import re,json,os
from .process import *

opt = os.path.join(os.path.expanduser("~"), 'Desktop','blog_opt')

def isExists():
    global opt
    if os.path.exists(opt):
        pass
    else:
        os.mkdir(opt)

def newjson(file):

    with open(file,'r',encoding='utf-8')as f:
        t = f.read()
    m = xmltodict.parse(t)["search"]

    tmp = []
    for i in m["entry"]:
        title = i["title"]
        url0 = parse.unquote(i["url"])
        url1 = re.sub(r'/.*?/.*?/.*?/','',url0,0,re.I).replace("/","")
        content_b = i["content"]["#text"][:25]
        md = read_md(os.path.join(opt,'posts/') + url1 + ".md")
        txt = blog_content(md)
        try:
            content = abstract(txt)
        except:
            content = content_b
        all = {"title":title,"url":url1,"content":content}
        tmp.append(all)

    isExists()
    with open(os.path.join(opt,"blog.json"),"w",encoding="utf-8")as f:
        json.dump(tmp,f,ensure_ascii=False,indent=4)


def newpy(file):
    with open(file, 'r', encoding='utf-8')as f:
        t = f.read()

    m = xmltodict.parse(t)["search"]

    tmp = []
    for i in m["entry"]:
        title = i["title"]
        url0 = parse.unquote(i["url"])
        url1 = re.sub(r'/.*?/.*?/.*?/', '', url0, 0, re.I).replace("/", "")
        content_b = i["content"]["#text"][:25]
        md = read_md(os.path.join(opt,'posts/') + url1 + ".md")
        txt = blog_content(md)
        try:
            content = abstract(txt)
        except:
            content = content_b
        all = {"title": title, "url": url1, "content": content}
        tmp.append(all)
    isExists()
    with open(os.path.join(opt,'blog.py'), 'w', encoding='utf-8')as f:
        f.write('bloglist = ')
        json.dump(tmp, f, indent=4, ensure_ascii=False)
