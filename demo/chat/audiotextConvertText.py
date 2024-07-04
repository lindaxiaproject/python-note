from pathlib import Path
import requests


def get_s2t_whisper():
    s2t_url = "http://192.168.8.125:28761/inference"
    input_file = Path(f'/Users/linhong/Desktop/16Hz_lizheng_26.wav')
    files = {'file': open(input_file, 'rb')}
    params = {
        'temperature': '0.0',
        'temperature_inc': '0.2',
        'response_format': 'json'
    }
    response = requests.post(url=s2t_url, files=files, params=params)
    if response.status_code == 200:
        json_response = response.json()
        print(json_response["text"])
        response_text = json_response["text"]
    else:
        print(f"s2t_whisper Request failed with status code {response.status_code}")
        response_text = response.status_code
    return response_text


if __name__ == '__main__':
    spe_txt = get_s2t_whisper()
    print(f'{spe_txt=}')
