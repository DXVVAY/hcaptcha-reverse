import xxhash
import json

def hash(data: str) -> str:
    return str(xxhash.xxh64_intdigest(json.dumps(data, separators=(",", ":")), seed=5575352424011909552))

#usecase
hashed = hash("[['HTML', 2], ['HEAD', 2], ['SCRIPT', 0], ['SCRIPT', 0], ['BODY', 0]]")
print(hashed)

# Output: 14773843042331491151