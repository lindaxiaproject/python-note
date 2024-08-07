import json

import requests

"""
headers = {
		"x-rapidapi-key": "e4ed8ce0bemsheafa74e1eb222e1p12e9cfjsn9954b3405cd1",
		"x-rapidapi-host": "vanitysoft-boundaries-io-v1.p.rapidapi.com"
	}
"""
if __name__ == '__main__':
	url = "https://faceanalyzer-ai.p.rapidapi.com/faceanalysis"

	payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"url\"\r\n\r\nhttps://openmediadata.s3.eu-west-3.amazonaws.com/face.jpg\r\n-----011000010111000001101001--\r\n\r\n"

	headers = {
		"x-rapidapi-key": "e4ed8ce0bemsheafa74e1eb222e1p12e9cfjsn9954b3405cd1",
		"x-rapidapi-host": "faceanalyzer-ai.p.rapidapi.com",
		"Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
	}

	# POST请求
	response = requests.post(url, data=payload, headers=headers)

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

