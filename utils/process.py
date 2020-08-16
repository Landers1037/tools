# 处理函数
from functools import reduce
import re


# 博客的md文件处理函数
def read_md(file):
    with open(file,encoding='utf-8')as md_file:
        content = reduce(lambda x,y: x+y,md_file.readlines())
        # content = md_file.readlines()

    return content

def blog_title(content):

    title = re.search(r'title: (.*)',content,re.M|re.I)
    return title.group(1)

def blog_content(content):

    post = re.sub(r'^---\n.*^---$',"",content,0,re.M|re.S)
    return post.replace("/static/res/blog/","/images/")

def blog_date(content):

    date = re.search(r'date: (.*) ',content,re.M|re.I)
    return date.group(1)

def abstract(content):
        # 摘要文字
        txt = blog_content(content)
        try:
            abstract = re.search(r'(.*)<!--more-->',txt,re.M|re.S|re.I).group(1)
        except:
            abstract = "<code>Sorry</code>该文章暂无概述💊"

        return abstract.replace("/static/res/blog/","/images/")
def tag(content):
    #标签
    try:
        tags = re.search(r'^tags:\n(.*)\ncategories',content,re.M|re.I|re.S).group(1)
        tags = re.sub(r'^url:.*id:.*',"",tags,0,re.M|re.S)
        tags = tags.replace('\n','').replace(' ','').split('-')[1:]
    except:
        tags = ['暂时没有标签']
    return tags


