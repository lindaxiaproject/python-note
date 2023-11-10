import requests
import json

def chat_stream(message: str, history=[], id=123, mark: bytes = b'$$%$'):
    # assert
    assert isinstance(mark, bytes)
    url = "http://192.168.8.125:9010/kb/api/chat"
    params = {"message": message, "history": history, "id": id,
              "token": '57d3d17868206f5e181fd27d0cbdde89d9739b0538b27ddd'}
    params = json.dumps(params)
    response = requests.post(url, data=params, stream=True)
    stream_content = b''
    for i in response.iter_content():
        stream_content += i
        if len(stream_content) > len(mark) and stream_content[-len(mark):] == mark:
            text = stream_content.split(mark)[0]
            result = json.loads(text)
            stream_content = b''
            yield result

if __name__ == '__main__':
    iters = chat_stream('你好')
    for i in iters:
        print(i)
