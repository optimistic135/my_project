import base64

# 要解码的Base64字符串
encoded_str = 'AnU7NnR4NassOGp3BDJgAGonMaJayTwrBqZ3ODMoMWxgMnFdNqtdMTM9'

# 使用base64解码
decoded_bytes = base64.b64decode(encoded_str)
decoded_str = decoded_bytes.decode('latin1')  # 例如，如果原始数据是ISO-8859-1编码

print(decoded_str)