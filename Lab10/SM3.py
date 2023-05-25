




def S(M,n):#32bit cycle_shift
    res=((M<<n)|(M>>(32-n)))&0xFFFFFFFF
    return res

def P(X,mode):
    if mode ==0:
        return X ^ S(X, 9) ^ S(X, 17)
    elif mode==1:
        return X ^ S(X, 15) ^ S(X, 23)
    return 0
def T(j):
    if 0<=j<16:
        return 0x79cc4519
    elif 16<=j<64:
        return 0x7a879d8a
    return 0
def FF(X,Y,Z,j):
    if 0 <= j < 16:
        return X^Y^Z
    elif 16 <= j < 64:
        return (X&Y)|(X&Z)|(Y&Z)
    return 0
def GG(X,Y,Z,j):
    if 0 <= j < 16:
        return X ^ Y ^ Z
    elif 16 <= j < 64:
        return (X & Y) | (~X & Z)
    return 0
def sm3_padding(msg):
    msg_len=len(msg)
    pad_num=64-((msg_len+8)%64)
    padding=b'\x00'*(pad_num-1)
    M=msg+b'\x80'+padding+int.to_bytes(msg_len*8,8,'big')
    return M
def sm3_extend(M):#输入64字节
    W=[int.from_bytes(M[i*4:i*4+4],'big') for i in range(len(M)//4)]
    W+=[0]*(68-len(M)//4)
    Wp=[0]*(64)
    for i in range(16,68):
        t=P(W[i-16]^W[i-9]^S(W[i-3],15),1)
        t=t^S(W[i-13],7)^W[i-6]
        W[i]=t
    for i in range(64):
        Wp[i]=W[i]^W[i+4]
    return W,Wp
def sm3_round(W,Wp,state):
    A,B,C,D,E,F,G,H=state
    for j in range(64):
        SS1=S((S(A,12)+E+S(T(j),j%32))%(1 << 32),7)
        SS2=SS1^S(A,12)
        TT1=(FF(A,B,C,j)+D+SS2+Wp[j]) %(1 << 32)
        TT2=(GG(E,F,G,j)+H+SS1+W[j]) % (1 << 32)
        D=C
        C=S(B,9)
        B=A
        A=TT1
        H=G
        G=S(F,19)
        F=E
        E=P(TT2,0)
    return [A^state[0],B^state[1],C^state[2],D^state[3],E^state[4],F^state[5],G^state[6],H^state[7]]
def sm3_digest(msg):
    IV = [0x7380166f, 0x4914b2b9, 0x172442d7, 0xda8a0600, 0xa96f30bc, 0x163138aa, 0xe38dee4d, 0xb0fb0e4e]
    state=IV
    msg=sm3_padding(msg)
    msg_len = len(msg)
    msg=[msg[i*64:i*64+64] for i in range(len(msg)//64)]
    for i in range(msg_len//64):
        W,Wp=sm3_extend(msg[i])
        state=sm3_round(W,Wp,state)
    digest=b''.join(list(map(lambda x:int.to_bytes(x,4,'big'),state)))
    return digest

def main():
    m=input().encode()
    print(sm3_digest(m))

if __name__ == '__main__':
    main()
