# -*- coding: utf-8 -*-
# Time: 2020-08-15 21:19
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: static_file.py

import requests
import os

def send_file(file,url):
    try:
        file = {
           os.path.basename(file) : (file, open(file,"rb"))
        }
        headers = {"checkme": "mgekx","Referer": "127.0.0.1"}
        r = requests.post(url=url,data=None,files=file, headers=headers)
        print(r.status_code)
        return True

    except Exception as e:
        print(r.status_code)
        return False
