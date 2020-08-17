# -*- coding: utf-8 -*-
# Time: 2020-08-17 19:21
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: hls.py

import subprocess,os

def hls(name=None):
    """
    默认在当前路径下执行
    :param file:
    :param name:
    :return:
    """
    file = os.listdir(os.getcwd())
    for f in file:
        if "mp4" in f and os.path.isfile(f):
            if name:
                pass
            else:
                name = os.path.basename(f).replace(".mp4","")

            cmd = "ffmpeg -i {} -force_key_frames \"expr:gte(t,n_forced*1)\" -c:v libx264 -c:a aac -strict -2 -f hls -hls_list_size 0 -hls_time 2 -hls_segment_filename {}_%3d.ts {}.m3u8".format(f,name,name)
            o = subprocess.getoutput(cmd)
            print(o)
        else:
            pass