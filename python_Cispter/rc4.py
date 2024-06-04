def swap_bytes(a, b):
    return (b << 8) | (a & 0xFF)


def KSA(key):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]  # Swap bytes
    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # Swap bytes
        t = (S[i] + S[j]) % 256
        K = S[t]
        yield K


def RC4_encrypt_decrypt(data, key, decrypt=False):
    S = KSA(key)
    keystream = PRGA(S)
    output = []
    for byte in data:  # 直接迭代字节，而不是字符
        K = next(keystream)
        if decrypt:
            output.append(byte ^ K)  # 直接对字节进行异或操作
        else:
            output.append(byte ^ K)
    return bytes(output)  # 返回字节串而不是字符串


# 示例密钥（应该是随机的字节串）
key = b'cryptography'


# 原始文本消息
plaintext = 'Hi,this is RC4!'

# 将文本编码为字节串
plaintext_bytes = plaintext.encode('utf-8')

# 加密文本
ciphertext_bytes = RC4_encrypt_decrypt(plaintext_bytes, key)
print(f'加密(hex): {ciphertext_bytes.hex()}')
print(f'加密(chars): {"".join(chr(b) for b in ciphertext_bytes )}')

# 解密文本
decrypted_bytes = RC4_encrypt_decrypt(ciphertext_bytes, key, decrypt=True)
decrypted_text = decrypted_bytes.decode('utf-8')
print(f'解密: {decrypted_text}')