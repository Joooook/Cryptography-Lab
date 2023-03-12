PC_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

PC_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

SHIFT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def replace(data,table,n):
    rData=0
    for i in range(len(table)):
        rData=rData | (data>>(n-table[i]) & 1)
        rData=rData<<1
    return rData>>1
def inv_replace(data,table,n):  #n置换前的长度
    rData=0
    for i in range(len(table)):
        rData=rData | (((data>>(len(table)-i-1)) & 1)<<(n-table[i]))
    return rData

def cycle_shift(data,n): #28位循环移n位
    sData=data
    for i in range(n):
        sData=((sData << 1) | sData >> (28 - 1))&0xFFFFFFF
    return sData

def init_key(key):
    keyList=[]
    rKey=replace(key,PC_1,64)#压缩
    C=rKey>>28              #分组
    D=rKey & 0xFFFFFFF
    for i in range(16):
        C=cycle_shift(C, SHIFT[i])
        D=cycle_shift(D, SHIFT[i])
        keyList.append(replace(C<<28 | D,PC_2,56))
    return keyList
def parity_check(key):
    k=key
    for i in range(8):
        checkByte=k & 0xFF
        count=0
        for j in range(8):
            if checkByte & 1==1:
                count+=1
            checkByte=checkByte>>1
        if count % 2==0:
            return False
        k=k>>8
    return True
def add_parity(key):
    list=[]
    for i in range(256):
        check=key
        for j in range(8):
            check=check | ((i>>(7-j))&1)<<((7-j)*8)
        if parity_check(check):
            list.append(check)
    return list

if __name__ == '__main__':
    #要让subkey一样，由于置换具有可逆性，所以在置换前就需要保持相等
    #也就是说，每次shift都要相等
    #
    sum=0
    sameList=[]
    tmp=[]
    for i in SHIFT:
        sum=(sum+i)%28
        sameList.append(sum)
    for i in sameList:
        sum= i % 28
        for j in SHIFT:
            sum =(sum + j) % 28
            if sum not in sameList:
                sameList.append(sum)
    sameList.sort()         #找出相同的
    halfWeakKey=[]
    for i in range(2):          #求出一半的弱密钥
        key=['2']*28
        for j in range(28):
            if j in sameList:
                key[j] =str(i)
        halfWeakKey.append(''.join(key))
    weakKey=[]
    for i in halfWeakKey:       #组合两半 弱密钥
        for j in halfWeakKey:
            weakKey.append(i+j)
    weakKeyWithParity = []
    for i in weakKey:
        weakKeyWithParity.append(add_parity(inv_replace(int(i,2),PC_1,64)))
    #以下是半弱密钥推导
    #半弱密钥在密钥Round中只产生两种密钥，假设第i轮和第j轮的密钥是相同的，推导所有可能
    #invshift是shift表格的逆方向
    INV_SHIFT = [1,2,2,2,2,2,2,1,2,2,2,2,2,2,1,1]
    #k1和k2分别为正负密钥
    k1Place=[i for i in range(28)]
    k2Place = [i for i in range(28)]
    count1=29
    count2=0
    for i in range(len(SHIFT)):
        count1-=SHIFT[i]
        count2+=SHIFT[i]
        shift1=[]
        shift2=[]
        for j in range(28):
            shift1.append((k1Place[j]+count1)%28)
            shift2.append((k2Place[j]+count2)%28)
        print(shift1)
        print(shift2)
        print()