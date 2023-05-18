import hashlib
def quick_pow(a, b, N):#快速模幂
    ans = 1
    while b:
        if b & 1:
            ans = ans * a % N
        a = a * a % N
        b = b >> 1
    return ans


def xor(a,b):
    return padding( int(a,16)^int(b,16),len(a)//2)[2:]#注意这里异或后可能会少一个最前面的0，所以要用padding

def MGF(mgfSeed,maskLen):#掩码函数
    seed=int(mgfSeed,16)
    res=''
    counter=0
    while len(res)<maskLen:
        res+=hashlib.sha1(int.to_bytes(seed<<32 | counter,(len(mgfSeed)//2)+4,'big')).hexdigest()
        """
        形式如Hash(mgfSeed||0x00000000) || Hash(mgfSeed||0x00000001) || Hash(mgfSeed||0x00000002)... Hash(mgfSeed||n)
        """
        counter+=1
    return res[:maskLen]#取前面的对应长度即可

def OAEP_encode(l,M,k,seed):
    lHASH=hashlib.sha1(l).hexdigest()
    hlen=len(lHASH)//2
    mlen=len(M)//2
    DB=lHASH+'00'*(k-2*hlen-2-mlen)+'01'+M
    maskedDB=xor(DB, MGF(seed,len(DB)))
    maskedSeed=xor(seed , MGF(maskedDB,len(seed)))
    EM='00'+maskedSeed+maskedDB
    return EM
def OAEP_decode(l,EM):
    lHASH = hashlib.sha1(l).hexdigest()
    hlen = len(lHASH) // 2
    maskedDB=EM[2+hlen*2:]
    maskedSeed=EM[2:hlen*2+2]
    seed = xor(maskedSeed, MGF(maskedDB, len(maskedSeed)))
    DB = xor(maskedDB, MGF(seed, len(maskedDB)))
    DB_check(DB,lHASH)
    tmp=DB[hlen*2:]
    return '0x'+tmp[tmp.find('1')+1:].lstrip('0')
def DB_check(DB,lHASH):#检查解密出来的DB是否合规
    #print(DB[:len(lHASH)])
    if DB[:len(lHASH)]!=lHASH:#是否能拆分lHash
        print('Ree')
        exit()
    tmp=DB[len(lHASH):]
    while tmp[:2]=='00':
        tmp=tmp[2:]
    if tmp[:2]!='01':#是否有ps
        print('Ree')
        exit()

def L_check(L,op):      #对l的长度检测
    if (len(L)-2)//2 > ((1<<61)-1):
        if op==1:
            print('Err')
        else:
            print('Ree')
        exit()
def M_check(M,k,seed):#对M的长度检测
    mLen=len(M)//2
    hLen=len(seed)//2
    if mLen>k-2*hLen-2:
        print('Err')
        exit()

def C_check(C,k):#对C的长度检测
    if len(C)//2!=k:
        print('Ree')
        exit()

def k_check(k,L):#对k的大小检测
    if L!=b'':
        hLen=len(hashlib.sha1(L).hexdigest())//2
        if k<2*hLen+2:
            print('Ree')
            exit()
def EM_check(EM):#对掩码的头检测
    if EM[:2]!='00':
        print('Ree')
        exit()

def RSA_encrypt(m,key,N):
    return quick_pow(m, key, N)

def RSA_decrypt(c,key,N):
    return quick_pow(c, key, N)

def padding(msg,k):#k字节补位
    return '0x' + hex(msg)[2:].rjust(k * 2, '0')

def main():
    op=int(input())
    k = int(input())
    key = int(input(),16)
    N = int(input(),16)
    R = input()[2:]#recive
    L=  input()
    if L=='0x':
        L=b''
    else:
        L_check(L,op)
        L=int.to_bytes(int(L,16), len(L[2:])//2, 'big')
    if op==1:
        M=R
        seed=input()[2:]
        M_check(M, k, seed)
        C=RSA_encrypt(int(OAEP_encode(L,M,k,seed),16),key,N)
        print(padding(C,k))
    else:
        C=R
        C_check(C,k)
        k_check(k,L)
        EM=padding(RSA_decrypt(int(C,16),key,N),k)[2:]
        EM_check(EM)
        print(OAEP_decode(L,EM))
if __name__ == '__main__':
    main()