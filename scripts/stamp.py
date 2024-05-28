from time import strftime, localtime, time
from string import ascii_letters
from math import ceil
import hashlib
import base64
import random
import json

def get_salt(salt_length: int) -> str:
    charset = ascii_letters + "+/="
    return ''.join([random.choice(charset) for _ in range(salt_length)])

def mint_stamp(challenge: str, bits: int) -> str:
    counter = 0
    hex_digits = int(ceil(bits / 4.0))
    zeros = '0' * hex_digits
    while 1:
        digest = hashlib.sha1((challenge + hex(counter)[2:]).encode()).hexdigest()
        if digest[:hex_digits] == zeros:
            return hex(counter)[2:]
        counter += 1

def mint(resource: str, bits: int = 2, ext: str = '', salt_chars: int = 8) -> str:
    timestamp = strftime("%Y-%m-%d", localtime(time()))
    challenge = f"1:{bits}:{timestamp}:{resource}:{ext}:{get_salt(salt_chars)}:"
    return f"{challenge}{mint_stamp(challenge, bits)}"


#usecase
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmIjowLCJzIjoyLCJ0IjoidyIsImQiOiIxMWV0QytPYTNhVWdHd2M3TFF1Tms2aUgvWmQvMm1LeUFFdllZRDBKOGdUcE4yK2xEcXBNZmxuVFpnY2NBQUlaUW9GeVRpb3E3WmNyTkthc2xHOVhkKzFLK3FXVUp2eFFqUmVLeXhWSkZsd1NVOGJTSll0VkN2WnZaTlRmbURhbGliY2MzNUpIbEl0bE92d1ZZVkJTRzU4MFZrMG9CT254cHV3MFdGbWJtejRjam9IVlF0S05BZGpCOW9ieUFob1R6elE1enpDSmhnc042SWE5MDVobDZXWlN3WHRwSzFlOEVmd2ZzUnNpcXBIeEJQQ2MwOVo2Q2hBN1lOU1FoVFdlIiwibCI6Imh0dHBzOi8vbmV3YXNzZXRzLmhjYXB0Y2hhLmNvbS9jL2Y5MjJhNDEiLCJpIjoic2hhMjU2LVF0bWtBUnJEYXVTRDZPUExTN0t6Z3B1V3Z6WnJ2QndPS3JRTlRYM3Jra0E9IiwiZSI6MTcxNTYxNjY4MiwibiI6ImhzdyIsImMiOjEwMDB9.kO00qLSV_ogCVPzD5JnorvbSLyjU7gBHdtXhKgFdBuQ"
s = token.split(".")[1].encode()
s += b'=' * (-len(s) % 4)
parsed = json.loads(base64.b64decode(s, validate=False).decode())
hc_diff = parsed['s']
hc_data = parsed['d']
stamp = mint(hc_data, hc_diff)
print(stamp)
# Output:
# 1:2:2024-05-28:11etC+Oa3aUgGwc7LQuNk6iH/Zd/2mKyAEvYYD0J8gTpN2+lDqpMflnTZgccAAIZQoFyTioq7ZcrNKaslG9Xd+1K+qWUJvxQjReKyxVJFlwSU8bSJYtVCvZvZNTfmDalibcc35JHlItlOvwVYVBSG580Vk0oBOnxpuw0WFmbmz4cjoHVQtKNAdjB9obyAhoTzzQ5zzCJhgsN6Ia905hl6WZSwXtpK1e8EfwfsRsiqpHxBPCc09Z6ChA7YNSQhTWe::HyatDRZw:4
