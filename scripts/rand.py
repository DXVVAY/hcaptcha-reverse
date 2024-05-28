from zlib import crc32
import random
import numpy

def random_float() -> float:
    return random.uniform(0.0000000000000001, 0.9999999999999999)

def rand(hsw_str: str) -> str:
    return numpy.uint32(crc32(hsw_str.encode())) * 2.3283064365386963e-10

#usecase
data = {
    "rand": [
        random_float(),
        rand("the encrypted hsw str")
    ]
}
print(data)

# Output:
#{
#    "rand": [
#        0.37582791536757076,
#        0.5740331697743386
#    ]
#}