from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    # 检查是否有 upload_file 参数
    if 'upload_file' not in request.files:
        return jsonify({"code": 500, "message": "No file part"}), 400
    file = request.files['upload_file']

    # 如果用户没有选择文件，浏览器也会提交一个空的文件部分
    if file.filename == '':
        return jsonify({"code": 500, "message": "No selected file"}), 400

    # 获取文件名和后缀
    # test.mp3
    filename = file.filename
    content_length = file.content_length
    print("文件长度:", content_length)
    # 使用os.path.splitext()分离文件名和扩展名
    file_root, file_extension = os.path.splitext(filename)
    # 文件名（不含扩展名）: zhoujielun
    print("文件名（不含扩展名）:", file_root)
    file_extension = file_extension[1:] if file_extension else ''
    # 文件扩展名: mp3
    print("文件扩展名:", file_extension)

    # 检查是否有 authCode 参数
    authCode = request.form.get('authCode')
    if not authCode:
        return jsonify({"code": 500, "message": "authCode请求参数不能为空"}), 400

    print(f"[测试]authCode字段请求参数为：{authCode}")

    # 创建临时目录
    upload_folder = './tmp'
    os.makedirs(upload_folder, exist_ok=True)
    print('成功创建临时目录 tmp')

    if file:
        # 保存文件到本地
        filename = secure_filename(file.filename)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return jsonify({"code": 200, "message": "File uploaded successfully", "filename": filename}), 200


if __name__ == '__main__':
    app.run(debug=True)

