import re
import sys


def swap(lst,i,j):
    l=min(i,j)
    b=max(i,j)
    if l==b:
        return lst
    if b==len(lst)-1:
        return lst[:l] + [lst[b]] + lst[l + 1:b] + [lst[l]]
    return lst[:l]+[lst[b]]+lst[l+1:b]+[lst[l]]+lst[b+1:]
def RC4(seed):
    S=RC4_init(seed)
    i=0
    j=0
    sys.stdin.read(2)
    byte = sys.stdin.read(2)
    print('0x',end='')
    while byte!='':
        byte=int(byte,16)
        i=(i+1)%256
        j=(j+S[i])%256
        S=swap(S,i,j)
        t=(S[i]+S[j])%256
        print(hex(byte^S[t])[2:].rjust(2,'0'),end='')
        byte = sys.stdin.read(2)
    return
def RC4_init(seed):
    S=[]
    K=[]
    for i in range(256):
        S.append(i)
    for i in range(256):
        K.append(seed[i%len(seed)])
    j=0
    for i in range(256):
        j=(j+S[i]+K[i]) % 256
        S=swap(S,i,j)
    return S
def main():
    k=input()[2:]
    RC4(list(map(lambda x:int(x,16),re.findall(r'.{2}',k))))
if __name__ == '__main__':
    main()