def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        yield S[(S[i] + S[j]) % 256]

def encryptRC4(plaintext, key, hexformat=False):
    key, plaintext = bytearray(key), bytearray(plaintext)  # necessary for py2, not for py3
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    keystream = PRGA(S)
    return b''.join(b"%02X" % (c ^ next(keystream)) for c in plaintext) if hexformat else bytearray(c ^ next(keystream) for c in plaintext)

print(encryptRC4(b'John Doe', b'mypass'))                           # b'\x88\xaf\xc1\x04\x8b\x98\x18\x9a'
print(encryptRC4(b'\x88\xaf\xc1\x04\x8b\x98\x18\x9a', b'mypass'))   # b'John Doe'
