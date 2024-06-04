import math
import binascii

sbox = [[0xd6, 0x90, 0xe9, 0xfe, 0xcc, 0xe1, 0x3d, 0xb7, 0x16, 0xb6, 0x14, 0xc2, 0x28, 0xfb, 0x2c, 0x05, ],
        [0x2b, 0x67, 0x9a, 0x76, 0x2a, 0xbe, 0x04, 0xc3, 0xaa, 0x44, 0x13, 0x26, 0x49, 0x86, 0x06, 0x99, ],
        [0x9c, 0x42, 0x50, 0xf4, 0x91, 0xef, 0x98, 0x7a, 0x33, 0x54, 0x0b, 0x43, 0xed, 0xcf, 0xac, 0x62, ],
        [0xe4, 0xb3, 0x1c, 0xa9, 0xc9, 0x08, 0xe8, 0x95, 0x80, 0xdf, 0x94, 0xfa, 0x75, 0x8f, 0x3f, 0xa6, ],
        [0x47, 0x07, 0xa7, 0xfc, 0xf3, 0x73, 0x17, 0xba, 0x83, 0x59, 0x3c, 0x19, 0xe6, 0x85, 0x4f, 0xa8, ],
        [0x68, 0x6b, 0x81, 0xb2, 0x71, 0x64, 0xda, 0x8b, 0xf8, 0xeb, 0x0f, 0x4b, 0x70, 0x56, 0x9d, 0x35, ],
        [0x1e, 0x24, 0x0e, 0x5e, 0x63, 0x58, 0xd1, 0xa2, 0x25, 0x22, 0x7c, 0x3b, 0x01, 0x21, 0x78, 0x87, ],
        [0xd4, 0x00, 0x46, 0x57, 0x9f, 0xd3, 0x27, 0x52, 0x4c, 0x36, 0x02, 0xe7, 0xa0, 0xc4, 0xc8, 0x9e, ],
        [0xea, 0xbf, 0x8a, 0xd2, 0x40, 0xc7, 0x38, 0xb5, 0xa3, 0xf7, 0xf2, 0xce, 0xf9, 0x61, 0x15, 0xa1, ],
        [0xe0, 0xae, 0x5d, 0xa4, 0x9b, 0x34, 0x1a, 0x55, 0xad, 0x93, 0x32, 0x30, 0xf5, 0x8c, 0xb1, 0xe3, ],
        [0x1d, 0xf6, 0xe2, 0x2e, 0x82, 0x66, 0xca, 0x60, 0xc0, 0x29, 0x23, 0xab, 0x0d, 0x53, 0x4e, 0x6f, ],
        [0xd5, 0xdb, 0x37, 0x45, 0xde, 0xfd, 0x8e, 0x2f, 0x03, 0xff, 0x6a, 0x72, 0x6d, 0x6c, 0x5b, 0x51, ],
        [0x8d, 0x1b, 0xaf, 0x92, 0xbb, 0xdd, 0xbc, 0x7f, 0x11, 0xd9, 0x5c, 0x41, 0x1f, 0x10, 0x5a, 0xd8, ],
        [0x0a, 0xc1, 0x31, 0x88, 0xa5, 0xcd, 0x7b, 0xbd, 0x2d, 0x74, 0xd0, 0x12, 0xb8, 0xe5, 0xb4, 0xb0, ],
        [0x89, 0x69, 0x97, 0x4a, 0x0c, 0x96, 0x77, 0x7e, 0x65, 0xb9, 0xf1, 0x09, 0xc5, 0x6e, 0xc6, 0x84, ],
        [0x18, 0xf0, 0x7d, 0xec, 0x3a, 0xdc, 0x4d, 0x20, 0x79, 0xee, 0x5f, 0x3e, 0xd7, 0xcb, 0x39, 0x48]]

FK0 = 0XA3B1BAC6
FK1 = 0X56AA3350
FK2 = 0X677D9197
FK3 = 0XB27022DC

CK = [0x00070e15, 0x1c232a31, 0x383f464d, 0x545b6269, 0x70777e85, 0x8c939aa1, 0xa8afb6bd, 0xc4cbd2d9,
      0xe0e7eef5, 0xfc030a11, 0x181f262d, 0x343b4249, 0x50575e65, 0x6c737a81, 0x888f969d, 0xa4abb2b9,
      0xc0c7ced5, 0xdce3eaf1, 0xf8ff060d, 0x141b2229, 0x30373e45, 0x4c535a61, 0x686f767d, 0x848b9299,
      0xa0a7aeb5, 0xbcc3cad1, 0xd8dfe6ed, 0xf4fb0209, 0x10171e25, 0x2c333a41, 0x484f565d, 0x646b7279]

rk = [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0,
      0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]

def S(x):
    row = (x >> 4) & 0xf
    col = x & 0xf
    return sbox[row][col]


def t(x):
    a0 = (x >> 24) & 0xff
    a1 = (x >> 16) & 0xff
    a2 = (x >> 8) & 0xff
    a3 = (x >> 0) & 0xff

    return ((S(a0) << 24) | (S(a1) << 16) | (S(a2) << 8) | S(a3))

def L(B):
    return (B ^ ((B << 2) & 0xffffffff) ^ ((B << 10) & 0xffffffff) ^ ((B << 18) & 0xffffffff) ^ (
                (B << 24) & 0xffffffff))


def T(x):
    B = t(x)
    return L(B)


def L_(B):
    return (B ^ ((B << 13) & 0xffffffff) ^ ((B << 23) & 0xffffffff))


def T_(x):
    B = t(x)
    return L_(B)


def K(MK0, MK1, MK2, MK3):
    K = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    K[0] = MK0 ^ FK0
    K[1] = MK1 ^ FK1
    K[2] = MK2 ^ FK2
    K[3] = MK3 ^ FK3
    for i in range(32):
        rk[i] = K[i + 4] = K[i] ^ T_(K[i + 1] ^ K[i + 2] ^ K[i + 3] ^ CK[i])


def SM4(x):  # SM4加密
    X = [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0,
         0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
    X[0] = (x >> 96) & 0xffffffff
    X[1] = (x >> 64) & 0xffffffff
    X[2] = (x >> 32) & 0xffffffff
    X[3] = (x >> 0) & 0xffffffff
    for i in range(32):
        X[i + 4] = X[i] ^ T(X[i + 1] ^ X[i + 2] ^ X[i + 3] ^ rk[i])
    Y = (X[35] << 96) ^ (X[34] << 64) ^ (X[33] << 32) ^ X[32]
    return Y


def SM4Decode(x):  # SM4解密
    X = [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0,
         0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
    X[0] = (x >> 96) & 0xffffffff
    X[1] = (x >> 64) & 0xffffffff
    X[2] = (x >> 32) & 0xffffffff
    X[3] = (x >> 0) & 0xffffffff
    for i in range(32):
        X[i + 4] = X[i] ^ T(X[i + 1] ^ X[i + 2] ^ X[i + 3] ^ rk[31 - i])
    return (X[35] << 96) ^ (X[34] << 64) ^ (X[33] << 32) ^ X[32]


# PKCS7填充方法
def BitsFill(P):
    # 将用户输入字符串填充到16的整数倍位（即16进制32位，二进制128位整数倍）
    """
    若字符串位数正好是16的倍数，则填充16个0x10对应的字符
    否则，不足位用【16-最后一段字符数】对应的字符填充
    填充用的字符命名为fillByte
    """

    if len(P) % 16 == 0:
        fillByte = chr(0x10)
        dataFill = "{0:{1}<{2}}".format(P, fillByte, len(P) + 16)
    else:
        n = math.ceil(len(P) / 16)
        fillByte = chr(16 * n - len(P))
        dataFill = "{0:{1}<{2}}".format(P, fillByte, 16 * n)

    # 转换为十六进制字符串
    strHex = dataFill.encode().hex()
    print(f"填充后为（16进制）：\n{strHex}")
    print(f"长度为：{len(strHex)}")

    # 转换为十六进制数
    dataHex = int(strHex, 16)
    bits = len(strHex) * 4
    return dataHex, bits, fillByte

if __name__ == '__main__':
    newkey = input("请输入初始密钥:")

    while len(newkey) < 16:
        newkey += newkey  # 重复整个字符串
        if len(newkey) >= 16:
            break  # 当达到或超过目标长度时退出循环
    newkey = binascii.hexlify(newkey[:16].encode('utf-8')).decode()
    print("0x"+newkey)

    P = input("请输入明文: ")
    P, bits2, fill2 = BitsFill(P)
    temp = bits2

    C = ""
    print("密文为：")
    while (bits2 != 0):
        bits2 = bits2 - 128
        Pk = (P >> bits2) & 0Xffffffffffffffffffffffffffffffff
        C = C + hex(SM4(Pk))[2:]
    print("0x"+C)
    print(f"长度为：{len(C)}")

    bits2 = temp
    C = int(C, 16)
    P = ""
    print("明文还原为：")
    while (bits2 != 0):
        bits2 = bits2 - 128
        # Pk从左往右依次取128位
        Ck = (C >> bits2) & 0Xffffffffffffffffffffffffffffffff
        P = P + hex(SM4Decode(Ck))[2:]
    print("0x"+P)
    print(f"长度为：{len(P)}")

    P = binascii.a2b_hex(P).decode()
    fill2 = ord(fill2)
    print(f"明文：{P[:(len(P) - fill2)]}")
