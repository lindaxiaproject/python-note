from flask import request, Flask
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_files():
    # `request.files` 是一个字典，包含了所有上传的文件
    files = request.files.getlist('files')
    for file in files:
        # 写入到指定路径下
        file.save(os.path.join('./', file.filename))
    return 'Files uploaded successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8801)


'''
<!DOCTYPE html>
<html>
<body>

<h2>File Upload</h2>
<form action="http://localhost:8801/upload" method="post" enctype="multipart/form-data" accept-charset="UTF-8">
  Select file to upload:
  <input type="file" name="files" id="file" multiple="multiple" />
  <input type="submit" value="Upload" name="submit">
</form>
</body>

'''
