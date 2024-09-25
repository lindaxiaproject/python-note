from pathlib import Path
import requests

'''
    一、前端返回给后端（wav）
        (1) 前端传一个16Hz、wav格式音频
        (2) 调用此接口，语音转文本，再调用大模型chat接口
'''


def get_s2t_whisper():
    url = "http://192.168.8.126:7861/inference"

    # {"error":"failed to read WAV file"}
    file_path = Path(f'./front_16Hz_lizheng_26.wav')

    payload = {
        'temperature': '0.0',
        'temperature_inc': '0.2',
        'response_format': 'json'
    }

    files = [
        # mp3 音频帧格式 audio/mpeg 、
        ('file', ('front_16Hz_lizheng_26.wav', open(file_path , 'rb'), 'audio/wav') )
    ]

    headers = {
        # 'Content-Type': 'multipart/form-data'
    }
    response = requests.post(url=url, headers=headers, data=payload, files=files)

    if response.status_code == 200:
        json_response = response.json()
        print(response.content)
        response_text = json_response["text"]
    else:
        print(f"失败语音转文字：{response.content}")
        response_text = response.status_code
    return response_text


if __name__ == '__main__':
    spe_txt = get_s2t_whisper()
    print(f'{spe_txt=}')
