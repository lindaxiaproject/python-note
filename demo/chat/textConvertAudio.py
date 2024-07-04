import argparse
import base64
import io
import os
import queue
import random
import re
import time
import traceback
from datetime import date
from typing import Union
from pathlib import Path
import requests

#文本转语音CharTTS（服务器调用）
def get_t2s_chartts():

    #文本转语音服务地址
    t2v_url = "http://192.168.8.125:28763/v1/tts"
    # t2v_url = "http://127.0.0.1:8000/v1/tts"

    # 设置文件和参数
    params = {
        "text": "人生如逆旅，我亦是行人！",
        "spk": "female2",
        "style": "chat",
        "temperature": 0.3,
        "top_p": 0.5,
        "top_k": 20,
        "seed": 42,
        "format": "mp3",
        "bs": 8,
        "thr": 100,
        # "prompt1": "我是一个说话非常嗲的山东女孩，喜欢撸串和喝啤酒。",
        # "prompt2": "很喜欢交朋友。",
        # "prefix": "",
    }

    # 发送POST请求
    response = requests.get ( url=t2v_url, params=params )
    # 检查响应状态码
    if response.status_code == 200:
        print ( "t2s_chattts Request successful!" )

        # 保存音频
        output_file = Path ( f'/Users/linhong/Desktop/output.mp3' )
        output_file.parent.mkdir ( parents=True, exist_ok=True )
        with open (output_file.as_posix(), 'wb' ) as f:
            f.write(response.content )
        print (f'{output_file=}' )

    else:
        print ( f"t2s_chattts Request failed with status code {response.status_code}" )

    return output_file.as_posix()

if __name__ == '__main__':
    speech_path = get_t2s_chartts()
    print(f'{speech_path=}')