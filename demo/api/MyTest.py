import json

import json

import requests

if __name__ == '__main__':
    params_json = json.dumps(["Ahrefs"])
    # 设置正确的内容类型
    headers = {'Content-Type': 'application/json'}
    # 发送GET请求，包含查询参数 http://180.184.80.35:6688/aiquant-mark/doc.html
    response = requests.post('http://180.184.80.35:6688/aiquant-mark/api-result-data/list', data=params_json,
                             headers=headers)
    # 设置响应的编码格式
    response.encoding = 'UTF-8'

    # 检查响应状态码
    if response.status_code == 200:
        # 打印API返回的数据
        # print(response.text)
        pass
    else:
        print('请求失败:', response.status_code)
    print(json.loads(response.text))
    df = json.loads(response.text)['data']
    print(df)