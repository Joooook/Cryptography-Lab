import math


def sha1_f(x,y,z,r):
    if r<20:
        res=(x & y)|(~x & z)
    elif r<40:
        res=x^y^z
    elif r<60:
        res = (x & y) | (x & z) | (y & z)
    else:
        res = x ^ y ^ z
    return res
def sha1_padding(M):
    init_len=len(M)*8
    pad_text=M+b'\x80'
    while len(pad_text) % 64!=56:
        pad_text+=b'\x00'
    EM=pad_text+int.to_bytes(init_len,8,'big')
    return EM
def S(M,n):#32bit cycle_shift
    res=((M<<n)|(M>>(32-n)))&0xFFFFFFFF
    return res


def sha1_extend(M):#输入64字节
    W=[int.from_bytes(M[i*4:i*4+4],'big') for i in range(len(M)//4)]
    W+=[0]*(80-len(M)//4)
    for i in range(16,80):
        W[i]=W[i-3]^W[i-8]^W[i-14]^W[i-16]
        W[i]=S(W[i],1)
    return W
def sha1_round(W,H,K):
    a,b,c,d,e=H[0],H[1],H[2],H[3],H[4]
    for j in range(80):
        temp=S(a,5)+sha1_f(b,c,d,j)+e+W[j]+K[math.floor(j/20)]
        e=d
        d=c
        c=S(b,30)
        b=a
        a=temp % (1<<32)
    H[0]=(H[0] + a)% (1<<32)
    H[1]=(H[1] + b)% (1<<32)
    H[2]=(H[2] + c)% (1<<32)
    H[3]=(H[3] + d)% (1<<32)
    H[4]=(H[4] + e)% (1<<32)
    return H

def sha1(M):#字节流输入
    K=[0x5A827999,0x6ED9EBA1,0x8F1BBCDC,0xCA62C1D6]
    H=[0x67452301,0xEFCDAB89,0x98BADCFE,0x10325476,0xC3D2E1F0]
    EM=sha1_padding(M)
    EM=[EM[i*64:i*64+64] for i in range(len(EM)//64)]
    l=len(EM)
    for i in range(l):
        W=sha1_extend(EM[i])
        H=sha1_round(W,H,K)
    digest=''.join(list(map(lambda x:hex(x)[2:].rjust(8,'0'),H)))
    return digest
def main():
    m=input().encode()
    print(hashlib.sha1(m).hexdigest())
if __name__ == '__main__':
    main()