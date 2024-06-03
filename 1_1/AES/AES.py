from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encrypt(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    iv = cipher.iv
    return iv, ct_bytes

def aes_decrypt(iv, ct_bytes, key):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plain_text = unpad(cipher.decrypt(ct_bytes), AES.block_size)
    return plain_text.decode()

# 生成一个随机的AES密钥
key = get_random_bytes(16)

# 需要加密的字符串
plain_text = input('输入需要加密的字符串')

# 加密
iv, ct_bytes = aes_encrypt(plain_text, key)
print("加密后的字节串：", ct_bytes)

# 解密
decrypted_text = aes_decrypt(iv, ct_bytes, key)
print("解密后的字符串：", decrypted_text)
