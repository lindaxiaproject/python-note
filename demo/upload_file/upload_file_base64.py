from flask import request, Flask
import json
import base64

app = Flask(__name__)


@app.route('/kb/api/uploadZoneFile', methods=['POST'])
def upload_files():
    # 解析json对象数据
    data_dict = json.loads(request.get_data())
    byte_encode_files = data_dict['files']
    token = data_dict['token']
    # 遍历加密后base64编码后的数据-字典类型
    for file_name, byte_encode_file in byte_encode_files.items():
        base64_bytes = byte_encode_file.encode("utf-8")
        # base解密返回二进制文件
        str_bytes = base64.b64decode(base64_bytes)
        with open(file_name, 'wb') as f:
            f.write(str_bytes)
    return 'Files uploaded successfully'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8801)

""" java调用demo """
'''
    @Test
    public void loadFile() throws IOException {
        Map<String, String> map = new HashMap<>();
        File file = new File("src/test/java/test/other/file/铁安监79.docx");
        FileInputStream input = new FileInputStream(file);
        String encodeStrFile = FileBase64Util.encode2Str(IOUtils.toByteArray(input));
        map.put("铁安监79.docx", encodeStrFile);

        File file2 = new File("src/test/java/test/other/file/铁安监80.docx");
        FileInputStream input2 = new FileInputStream(file2);
        String encodeStrFile2 = FileBase64Util.encode2Str(IOUtils.toByteArray(input2));
        map.put("铁安监80.docx", encodeStrFile2);

        Map data = new HashMap();
        data.put("token", "57d3d17868206f5e181fd27d0cbdde89d9739b0538b27ddd");
        data.put("files", map);
        String finalData = JSON.toJSONString(data);
        CloseableHttpResponse response = EpsRestHttpClient.post("http://127.0.0.1:8801/upload", finalData, StandardCharsets.UTF_8);
        HttpEntity entity = response.getEntity();
        String responseContent = EntityUtils.toString(entity, "UTF-8");
        System.out.println(responseContent);
    }
'''
