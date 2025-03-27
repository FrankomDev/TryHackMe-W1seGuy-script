import string
import random

wanted = '057c2c0b'
globalKey = ''

def hash():
    global globalKey
    res = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    key = str(res)

    flag = 'THM{'
    xored = ''

    for i in range(0,len(flag)):
        xored += chr(ord(flag[i]) ^ ord(key[i%len(key)]))

    hex_encoded = xored.encode().hex()
    globalKey = key
    return hex_encoded

def findKey():
    while True:
        testvar = hash()
        if testvar == wanted:
            print('KEY is: '+ globalKey)
            break
            

findKey()


