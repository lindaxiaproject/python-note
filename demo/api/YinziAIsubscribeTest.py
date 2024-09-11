import requests
from PIL import Image
import io
import json

if __name__ == '__main__':

    headers = {
        "client-type": "WEB",
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ5b3VpZGlhbi5jb20iLCJtZW1iZXJOYW1lIjoi5Lya5ZGYM3kzN3JrIiwibWVtYmVySWQiOjYzNDE0NiwibWVtYmVyVWlkIjoieXo5NzQ5NDU1MyJ9.EUYox0DPatZDp-Z0x2GuO_dpg2jzi2Z97O5YvYLO0EY"
    }

    weixin_headers = {
        "client-type": "WEB",
        "sec-ch-ua-platform": "macOS"
    }
    response = requests.get('https://www.yinziai.com/yinziai-web/member/current', headers=headers)
    response.encoding = 'UTF-8'
    if response.status_code == 200:
        result = response.json()
        data_object = result.get('data', {})
        uid = data_object.get('uid', None)
        print('>>>>>>成功获取用户id:', uid)
        ticket_response = requests.get(
            'https://www.yinziai.com/yinziai-web/member/scan/ticket?scene=bind_web_' + uid + '&expireSeconds=300',
            headers=headers)
        ticket_response.encoding = 'UTF-8'
        if ticket_response.status_code == 200:
            ticket_result = ticket_response.json()
            ticket_data_object = ticket_result.get('data', {})
            ticket = ticket_data_object.get('ticket', None)
            print('>>>>>>成功获取微信凭据:', ticket)
            weixin_response = requests.get('https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=' + ticket, headers=weixin_headers)
            weixin_response.encoding = 'UTF-8'
            if weixin_response.status_code == 200:
                # weixin_result = weixin_response.json()
                # weixin_data_object = weixin_result.get('data', {})
                binary_jpg_image = weixin_response.content
                if binary_jpg_image:
                    image_stream = io.BytesIO(binary_jpg_image)
                    try:
                        image = Image.open(image_stream)
                        image.show()
                        image.save('./output.png')
                        print(weixin_response)
                    except IOError as e:
                        print(f"无法读取微信二维码图像: {e}")
            else:
                print('调用获取微信二维码API请求失败:', weixin_response.status_code)
        else:
            print('调用获取微信二维码凭据API请求失败:', ticket_response.status_code)

    else:
        print('调用用户数据API请求失败:', response.status_code)
