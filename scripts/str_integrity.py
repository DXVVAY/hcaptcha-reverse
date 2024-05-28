from urllib.parse import quote
import base64
import random

def encode(input_str: str) -> list:
    h_a, in_arr = 'abcdefghijklmnopqrstuvwxyz', ''.join(chr(random.randint(65, 90)) for _ in range(13))
    rand_a = random.randint(1, 26)
    result = []

    for char in input_str[::-1]:
        if char.isalpha():
            shifted_char = h_a[(h_a.index(char.lower()) + rand_a) % 26]
            result.append(shifted_char.upper() if char.isupper() else shifted_char)
        else:
            result.append(char)

    result = ''.join(result)[::-1]
    b64 = base64.b64encode(quote(result).encode()).decode()[::-1]
    b64rand = random.randint(1, len(b64) - 1)
    b64 = b64[b64rand:] + b64[:b64rand]

    output = [char.lower() if char.isupper() else char.upper() if char in in_arr or char in in_arr.lower() else char for char in b64]

    return [''.join(output), f"{rand_a:x}", f"{b64rand:x}", in_arr]

#usecase
str = encode("ANGLE (Intel, Intel(R) UHD Graphics (0x00008A56) Direct3D11 vs_5_0 ps_5_0, D3D11)")

print(str)

# Output: 
#[
#   'jXezszsemyuyqyucmfvzx6dhmyucmfvzx6ngmyusmXs0mhpgB5b3switjwfemyucm2azmwitjffuwwitjspwE21eBobJmlGeulb1qvbJmlmkmlGeulb1qvhJmlaJmlw0uovfs5it', 
#   '7', 
#   '3', 
#   'GTEMJBNGAJXUJ'
#]

# The output is always diffrent