def vernam_decrypt(s, key):
    count = 0
    l = len(key)
    m = ''
    for i in s:
        m+= chr(ord(i)^ord(key[count]))
        count = (count + 1) % l
    return m


def vernam_encrypt(s, key):
    count=0
    l=len(key)
    c = ''
    for i in s:
        c += chr(ord(i)^ord(key[count]))
        count=(count+1)%l
    return c
def main():
    key = input().strip()
    s = input().strip()
    op = int(input())
    if op == 0:
        print(vernam_decrypt(s, key))
    elif op == 1:
        print(vernam_encrypt(s, key))
