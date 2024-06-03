import random
import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

size=input('输入数据集大小:')
data = np.random.randint(0, 100, size=int(size))
print("原始数据: ", data)

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_ECB)

encrypted_data = [cipher.encrypt(pad(bytes([i]), AES.block_size)) for i in data]
print("加密后的数据: ", encrypted_data)

def range_query(encrypted_data, low, high):
    decrypted_data = [unpad(cipher.decrypt(i), AES.block_size)[0] for i in encrypted_data]
    return [i for i in decrypted_data if low <= i <= high]

low=(input('输入查询最小值：'))
high=(input('输入查询最大值：'))
print("范围查询结果: ", range_query(encrypted_data, int(low), int(high)))
