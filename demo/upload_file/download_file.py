import base64
import io

from flask import request, Flask, send_file, make_response
import json
import os
import zipfile

app = Flask(__name__)


@app.route('/download', methods=['POST'])
def download_directory():
    data_dict = json.loads(request.get_data())
    filename = data_dict['projectName']
    project_path = data_dict['projectPath']
    zip_buffer = io.BytesIO()
    # 创建ZIP文件并将其内容写入临时文件对象
    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        # 假设你想压缩的文件夹名为'directory_to_compress'
        for filename in os.listdir(project_path):
            file_path = os.path.join(project_path)
            zip_file.write(file_path, filename)

    # 将文件的当前位置设置到开始，以便读取
    zip_buffer.seek(0)
    # 将ZIP文件的内容转换为二进制
    binary_zip = zip_buffer.read()
    base64_encoded_zip = base64.b64encode(binary_zip).decode('utf-8')
    # 将base64编码的字符串转换回bytes
    response = make_response(base64_encoded_zip)
    #
    # # 设置响应的MIME类型为文本
    response.headers['Content-Type'] = 'text/plain'
    # # 设置提供内容的disposition为attachment并指定文件名
    response.headers['Content-Disposition'] = 'attachment; filename='+filename+'.zip'
    return base64_encoded_zip


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=18801)
