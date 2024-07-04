# 导入hashlib和base64模块
import hashlib
import base64
from sm4 import SM4Key
# 导入sm4模块，你可以从[这里](https://pypi.org/project/sm4/)或[这里](https://pypi.org/project/fastgm/)安装

def encryptDataBySM4(content, sourceKey):
    # 使用MD5算法对sourceKey进行散列，得到一个16进制的字符串hex16Key
    hex16Key = hashlib.md5(sourceKey).hexdigest()
    # 使用sm4模块的SM4Key方法，根据hex16Key的字节数组创建一个对象sm4
    sm4 = SM4Key(bytes.fromhex(hex16Key))
    # 使用sm4对象的encrypt方法，对content进行加密，并将加密后的字节数组转换为Base64编码的字符串
    return base64.b64encode(sm4.encrypt(content))


if __name__ == '__main__':
    sourceKey = "Hello, world!"
    content = "57d3d17868206f5e181fd27d0cbdde89d9739b0538b27ddd"
    print("加密："+  encryptDataBySM4(sourceKey,content))
