import gmpy2
import random

def generate_large_prime(size):
    #生成大奇数
    num = random.randrange(2 ** (size - 1), 2 ** size)
    if not gmpy2.is_odd(num):
        return generate_large_prime(size)
    else:
        if not gmpy2.is_prime(num,15):
            return generate_large_prime(size)
        else:
            print("素数为",num)
            return num

def get_srcertkey(p,q,e):
    fai_n = (p - 1) * ( q - 1)
    d = gmpy2.invert(e, fai_n)
    print("私钥为",d)
    return d

def encrypt(m, e, n):
    list = []
    for x in m:
        list.append(pow(ord(x), e, n))
    return list


# 用私钥(d,n)将密文cipher进行解密
def decrypt(cipher, d, n):
    m_string = ''
    for x in cipher:
        m_string += chr(pow(x, d, n))
    return m_string

if __name__ == '__main__':
    p = generate_large_prime(512)
    q = generate_large_prime(512)
    n = p * q
    e = (2 ** 16) + 1
    d = get_srcertkey(p=p, q=q, e=e)
    # message = input("请输入你想加密的内容：")
    m = "Hi, this is RSA!"
    print('准备加密的明文:', m)
    cipher = encrypt(m, e, n)
    print('加密后的密文(列表中每一项对应一个字符:)', cipher)
    m_decrypt = decrypt(cipher, d, n)
    print('解密后与原明文对比:', m_decrypt)



