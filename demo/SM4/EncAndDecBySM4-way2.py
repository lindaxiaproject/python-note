import hashlib
from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT

def encryptDataBySM4(content, sourceKey):
    # 使用MD5算法对sourceKey进行散列，得到一个16进制的字符串hex16Key
    hex16Key = hashlib.md5(sourceKey.encode()).hexdigest()
    # 将hex16Key转换为32字节的二进制数据
    key = bytes.fromhex(hex16Key)
    # 创建SM4对象
    sm4 = CryptSM4()
    # 设置密钥和模式
    sm4.set_key(key, SM4_ENCRYPT)
    # 加密内容并返回16进制编码
    return sm4.crypt_ecb(content.encode()).hex()


def decryptDataBySM4(ciphertext, sourceKey):
    # 使用MD5算法对sourceKey进行散列，得到一个16进制的字符串hex16Key
    hex16Key = hashlib.md5(sourceKey.encode()).hexdigest()
    # 将hex16Key转换为32字节的二进制数据
    key = bytes.fromhex(hex16Key)
    # 创建SM4对象
    sm4 = CryptSM4()
    # 设置密钥和模式
    sm4.set_key(key, SM4_DECRYPT)
    # 解密内容并返回原始数据
    return sm4.crypt_ecb(bytes.fromhex(ciphertext)).decode()

if __name__ == '__main__':
    print("加密："+  encryptDataBySM4("Hello, world!","57d3d17868206f5e181fd27d0cbdde89d9739b0538b27ddd"))
    print("解密：" + decryptDataBySM4("d9e20de9a2b7b4cb89966f0c72b63c48", "57d3d17868206f5e181fd27d0cbdde89d9739b0538b27ddd"))