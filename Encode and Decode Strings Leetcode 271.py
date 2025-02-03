# Encode and Decode Strings Leetcode 271
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
def encode(strs: list[str]) -> str:
    result = []
    for s in strs:
        result.append(str(len(s)) + '/' + s) # append the length of the string followed by '/' and the string itself
    print(''.join(result))
    return ''.join(result)

def decode(s: str) -> list[str]:
    result = []
    i = 0
    while i < len(s):
        slash = s.find('/', i)
        size = int(s[i:slash]) # get the size of the string
        result.append(s[slash+1:slash+1+size]) # extract the string using the size
        i = slash + 1 + size # update the index
    return result

def encode_decode(strs: list[str]) -> list[str]:
    encoded = encode(strs)
    decoded = decode(encoded)
    return decoded

# Time complexity: O(n) for encoding and decoding
# Space complexity: O(n) for encoding and decoding
# Approach: While encoding, append the length of the string followed by '/' and the string itself. While decoding, find the index of '/' and get the length of the string. Then, extract the string using the length and append it to the result list.

# Test cases
print(encode_decode(["hello", "world"])) # ["hello", "world"]
print(encode_decode(["leet", "code"])) # ["leet", "code"]
