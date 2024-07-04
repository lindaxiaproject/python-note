from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT

'''
    :function: 加密函数
    :param
        content: 元数据
        sourceKey: 自定义密钥串
'''
def encryptDataBySM4(content, sourceKey):
    # 将密钥转换为32字节的二进制数据
    key = sourceKey.encode()
    # 创建SM4对象
    sm4 = CryptSM4()
    # 设置密钥和模式
    sm4.set_key(key, SM4_ENCRYPT)
    # 加密内容并返回16进制编码
    return sm4.crypt_ecb(content.encode()).hex()

'''
    :function: 解密函数
    :param
        ciphertext: 加密后文本数据
        sourceKey: 自定义密钥串
'''
def decryptDataBySM4(ciphertext, sourceKey):
    # 将密文转换为二进制数据
    data = bytes.fromhex(ciphertext)
    # 将原始密钥转换为32字节的二进制数据
    key = sourceKey.encode()
    # 创建SM4对象，并设置密钥和模式
    sm4 = CryptSM4()
    sm4.set_key(key, SM4_DECRYPT)
    # 创建解密器，并对二进制数据进行解密
    decryptor = sm4.crypt_ecb(data)
    # 将解密后的二进制数据转换为字符串
    return decryptor.decode()


if __name__ == '__main__':
    print("加密前："+encryptDataBySM4("Hello, world!","57d3d17868206f5e181fd27d0cbdde89d9739b0538b27ddd"))
    print("解密后：" + decryptDataBySM4("680652c912f3dab95cc086f5eac6acfd", "57d3d17868206f5e181fd27d0cbdde89d9739b0538b27ddd"))


