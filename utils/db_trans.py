# -*- coding: utf-8 -*-
# Time: 2020-03-06 17:25
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: db_trans.py

from sqlalchemy import Column,dialects,create_engine,Integer,String,Text,Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json,os

from .process import *

opt = os.path.join(os.path.expanduser("~"), 'Desktop', 'blog_opt')
base = declarative_base()
engine = create_engine('sqlite:///'+os.path.join(opt,'app.db')) #数据库引擎
sessionfactory = sessionmaker(bind=engine) #session池
session = sessionfactory() #一个seesion用于操作数据库


class Posts(base):
    __tablename__ = 'posts'
    id = Column(Integer,primary_key=True)
    title = Column(String,nullable=False)
    url = Column(String,nullable=False)
    content = Column(String(500))
    pin = Column(Boolean,nullable=True)

class Tags(base):
    __tablename__ = 'tags'
    id = Column(Integer,primary_key=True)
    tag = Column(String,nullable=False)
    posturl = Column(String)
    title = Column(String)
    content = Column(String(200))

class Post(base):
    __tablename__ = 'post'
    id = Column(Integer,primary_key=True)
    title = Column(String(100))
    url = Column(String,nullable=False)
    content = Column(Text)
    date = Column(String(40))


class Uv(base):
    __tablename__ = 'uv'
    id = Column(Integer,primary_key=True)
    count = Column(Integer)
    name = Column(String)

class Message(base):
    __tablename__ = "message"
    id = Column(Integer, primary_key=True)
    mes = Column(Text)


def create():
    """
    新建一个数据库文件
    :return:
    """
    base.metadata.create_all(engine)


def init_posts():
    """
    根据json生成数据库的posts表
    :return:
    """
    with open(os.path.join(opt,"blog.json"),'r',encoding='utf-8')as f:
        data = json.load(f)
        for d in data:
            title = d["title"]
            url = d["url"].replace("/","")
            content = d["content"]
            if url == 'pin':
                onepost = Posts(title=title,url=url,content=content,pin=True)
            else:
                onepost = Posts(title=title,url=url,content=content,pin=False)
            session.add(onepost)
            session.commit()

def init_article():
    """
    文章写入到post文章表里
    :return:
    """
    if os.path.exists(os.path.join(opt,'posts')):
        list = os.listdir(os.path.join(opt,"posts"))

        for i in list:
            md = read_md(os.path.join(opt,"posts/")+i)
            content = blog_content(md)
            date = blog_date(md)
            title = blog_title(md)
            url = i.replace(".md","")
            p = Post(title=title,date=date,url=url,content=content)
            session.add(p)
            session.commit()

def tags():
    """
    标签写入到tag表里
    :return:
    """
    if os.path.exists(os.path.join(opt, 'posts')):
        list = os.listdir(os.path.join(opt,"posts"))
        for i in list:
            md = read_md(os.path.join(opt,"posts/")+i)
            url = i.replace(".md","")
            tags = tag(md)
            title = blog_title(md)
            content = abstract(md)
            for t in tags:
                session.add(Tags(tag=t,posturl=url,title=title,content=content))
                session.commit()

def uv(num):
    """
    用户访问量的统计表
    :return:
    """
    num = int(num)
    uv = Uv(count=num,name="uv")
    session.add(uv)
    session.commit()

def mes():
    """
    留言表
    :return:
    """
    m = Message(mes="你好，这里是我的博客留言板")
    session.add(m)
    session.commit()

def upposts():
    """
    按目录读取更新全部文章
    直接强制更新全部 不用匹配更新
    :return:
    """
    if os.path.exists(os.path.join(opt, 'blog.json')):
        posts_list = session.query(Posts).all()
        for p in posts_list:
            session.delete(p)
        session.commit()

        with open(os.path.join(opt,"blog.json"),'r',encoding='utf-8')as f:
            data = json.load(f)
            for d in data:
                try:
                    # flag = session.query(Posts).filter(Posts.url == d["url"].replace("/", "")).first()
                    title = d["title"]
                    url = d["url"].replace("/", "")
                    content = d["content"]
                    onepost = Posts(title=title, url=url, content=content, pin=False)
                    session.add(onepost)
                    session.commit()
                except  Exception as e:
                    pass


def uppost(post):
    """
    指定名称post，实则为url
    :param post:
    :return:
    """
    if os.path.exists(os.path.join(opt, 'posts')):
        p = session.query(Post).filter(Post.url == post.replace("/", "")).first()
        if not p:
            #不存在则不更新
            #判断是不是新加的
            if os.path.exists(os.path.join(opt, "posts/") + post + ".md"):
                try:
                    md = read_md(os.path.join(opt, "posts/") + post + ".md")
                    content = blog_content(md)
                    date = blog_date(md)
                    title = blog_title(md)
                    new = Post(title=title, date=date, url=post, content=content)
                    session.add(new)
                    session.commit()
                    print("已更新")
                except:
                    pass
            else:
                print("本地文件不存在")
        else:
            try:
                md = read_md(os.path.join(opt, "posts/") + post + ".md")
                content = blog_content(md)
                date = blog_date(md)
                title = blog_title(md)

                p.title = title
                p.date= date
                p.content = content
                session.commit()
            except:
                session.rollback()


        list = os.listdir(os.path.join(opt,'posts'))
        for i in list:
            try:
                flag = session.query(Post).filter(Post.url == i.replace(".md", "")).first()
                if flag:
                    pass
                else:
                    md = read_md(os.path.join(opt,"posts/") + i)
                    content = blog_content(md)
                    date = blog_date(md)
                    title = blog_title(md)
                    url = i.replace(".md", "")
                    p = Post(title=title, date=date, url=url, content=content)
                    session.add(p)
                    session.commit()
            except:
                pass

def uptags():
    if os.path.exists(os.path.join(opt, 'posts')):
        list = os.listdir(os.path.join(opt,'posts'))
        for i in list:
            try:
                flag = session.query(Tags).filter(Tags.posturl == i.replace(".md", "")).first()
                if flag:
                    pass
                else:
                    md = read_md(os.path.join(opt,"posts/") + i)
                    url = i.replace(".md","")
                    tags = tag(md)
                    title = blog_title(md)
                    content = abstract(md)
                    for t in tags:
                        session.add(Tags(tag=t,posturl=url,title=title,content=content))
                        session.commit()
            except:
                pass

def upuv(num):
    uv = session.query(Uv).first()
    uv.count = int(num)
    session.add(uv)
    session.commit()


###初始化新的数据库
def newDB():
    try:
        os.remove(os.path.join(opt,"app.db"))
    except:
        pass
    create()
    init_posts()
    init_article()
    tags()
    uv(1)
    mes()

    session.close()

###更新文章
def updateDB(ps=None,p=None,t=None,u=None):
    #posts表不能更新因为id 1一定是pin
    try:
        if p:
            uppost(p)
        if ps:
            upposts()
        if t:
            uptags()
        if u:
            upuv(u)
    finally:
        session.close()

def blog_test():
    """
    选择有代表性的文章查看信息
    :return:
    """
    bl = session.query(Posts).all()
    for b in bl:
        print(b.title,b.url)

