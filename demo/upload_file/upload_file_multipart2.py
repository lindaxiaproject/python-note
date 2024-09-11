from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# 确保上传目录存在
upload_folder = './tmp'
os.makedirs(upload_folder, exist_ok=True)


@app.route('/upload', methods=['POST'])
def upload_file():
    
    if 'upload_file' not in request.files:
        return jsonify({"code": 500, "message": "No file part"}), 400
    file = request.files['upload_file']

    if file.filename == '':
        return jsonify({"code": 500, "message": "No selected file"}), 400

    if file:
        # 保存文件
        filename = secure_filename(file.filename)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return jsonify({"code": 200, "message": "File uploaded successfully", "filename": filename}), 200


if __name__ == '__main__':
    app.run(debug=True)

