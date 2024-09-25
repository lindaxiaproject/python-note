import requests
import json
import base64


class Base64UTIL:
    @staticmethod
    def encode(data: str) -> str:
        """
        对字符串进行Base64编码。

        :param data: 需要编码的字符串
        :return: Base64编码后的字符串
        """
        # 将字符串转换为字节
        data_bytes = data.encode('utf-8')
        # 进行Base64编码
        base64_bytes = base64.b64encode(data_bytes)
        # 将字节解码为字符串
        base64_string = base64_bytes.decode('utf-8')
        return base64_string

    @staticmethod
    def decode(encoded_data: str) -> str:
        """
        对Base64编码的字符串进行解码。

        :param encoded_data: Base64编码的字符串
        :return: 解码后的原始字符串
        """
        # 将Base64编码的字符串转换为字节
        encoded_bytes = encoded_data.encode('utf-8')
        # 进行Base64解码
        base64_decoded_bytes = base64.b64decode(encoded_bytes)
        # 将解码后的字节转换为字符串
        original_string = base64_decoded_bytes.decode('utf-8')
        return original_string

if __name__ == '__main__':
    api_url = 'http://127.0.0.1:6688/aiquant-mark/check-data/exeApiCurlCommand'
    with open('./curl_command.txt', 'r', encoding='utf-8') as file:
        api_command_by_txt = file.read()
    # print(api_command_by_txt)
    data = {
        'apiKey':  'da255e96c0mshdb05a5ab25cd314p1cdaa6jsne7fe9d24aac2',
        'apiCommand': Base64UTIL.encode(api_command_by_txt),
        'apiName': 'chat_tts gpt detector',
        'appName': 'AI Detection',
    }

    json_data = json.dumps(data)
    response = requests.post(api_url, headers={'Content-Type': 'application/json'}, data=json_data)
    if response.status_code == 200:
        print('请求成功!')
        print(response.json())
    else:
        print('失败调用接口:', response.status_code)
