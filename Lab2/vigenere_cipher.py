def vigenere_decrypt(s, key):
    count = 0
    l = len(key)
    m = ''
    for i in s:
        m+=chr((ord(i)-ord('a')-(ord(key[count])-ord('a')))%26+ord('a'))
        count = (count + 1) % l
    return m


def vigenere_encrypt(s, key):
    count=0
    l=len(key)
    c = ''
    for i in s:
        c += chr((ord(i)-ord('a')+ord(key[count])-ord('a'))%26+ord('a'))
        count=(count+1)%l
    return c


def main():
    key = input().strip()
    s = input().strip()
    op = int(input())
    if op == 0:
        print(vigenere_decrypt(s, key))
    elif op == 1:
        print(vigenere_encrypt(s, key))
