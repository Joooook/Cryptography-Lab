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

def sha1(M):#字节流输入#字节流输出
    K=[0x5A827999,0x6ED9EBA1,0x8F1BBCDC,0xCA62C1D6]
    H=[0x67452301,0xEFCDAB89,0x98BADCFE,0x10325476,0xC3D2E1F0]
    EM=sha1_padding(M)
    EM=[EM[i*64:i*64+64] for i in range(len(EM)//64)]
    l=len(EM)
    for i in range(l):
        W=sha1_extend(EM[i])
        H=sha1_round(W,H,K)
    digest=b''.join(list(map(lambda x:int.to_bytes(x,4,'big'),H)))
    return digest
def hmac_padding(K):#字节输入
    # sha1分组长度为512bit
    return K+b'\x00'*(64-len(K))


def xor(a,b,n):#n返回字节长度
    return int.to_bytes(int.from_bytes(a,'big')^int.from_bytes(b,'big'),n,'big')

def HMAC(K,M):
    #sha1分组长度为512bit
    ipad=b'\x36'*64
    opad = b'\x5C' * 64
    Kp=hmac_padding(K)
    Si=xor(Kp,ipad,64)
    S0=xor(Kp,opad,64)
    return sha1(S0+sha1(Si+M))

def main():
    K=input()
    K=int.to_bytes(int(K,16),len(K)//2,'big')
    M=input().encode()
    print(hex(int.from_bytes(HMAC(K,M),'big'))[2:].rjust(32,'0'))
if __name__ == '__main__':
    main()