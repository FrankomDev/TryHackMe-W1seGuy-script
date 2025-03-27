import string
hex_encoded = '057c2c0b2060550d1e24144c1531242500021b33105a1343313d781818052340184025234c2e022d'
key = 'Q4ap'

decoded_bytes = bytes.fromhex(hex_encoded)

numbers = ['0','1','2','3','4','5','6','7','8','9']
allCharacters = numbers + (list(string.ascii_letters))

for char in allCharacters:
    keyy = key+char
    decrypted = ""
    for i in range(len(decoded_bytes)):
        decrypted += chr(decoded_bytes[i] ^ ord(keyy[i % len(keyy)]))
    print('Key: '+keyy +' String: '+decrypted)

