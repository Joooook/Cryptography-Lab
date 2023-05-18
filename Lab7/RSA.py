import gmpy2
import random
def Egcd(a, b):
    c = a
    d = b
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1
    while c % d != 0:
        gcd = c % d
        q = c // d
        c = d
        d = gcd
        ppx = s0 - s1 * q
        s0 = s1
        s1 = ppx
        ppy = t0 - t1 * q
        t0 = t1
        t1 = ppy
    gcd = d
    return ppx, ppy, gcd


def invmod(a, n):
    inv, _, _ = Egcd(a, n)
    return inv % n

def quick_pow(a, b, N):
    ans = 1
    while b:
        if b & 1:
            ans = ans * a % N
        a = a * a % N
        b = b >> 1
    return ans

def CRT(A,M):
    N=1
    for i in M:
        N*=i
    ans=0
    for i in range(len(A)):
        ans+=A[i] * (N//M[i])*invmod(N//M[i],M[i])
    return ans%N

def RSA_encrypt(p,q,e,m):
    return quick_pow(m,e,p*q)

def RSA_decrypt(p,q,e,c):
    d=invmod(e,(p-1)*(q-1))
    return CRT([quick_pow(c,d%(p-1),p),quick_pow(c,d%(q-1),q)],[p,q])

def millerRabinTest(n, iter_num):
    if n == 2:
        return True
    if n & 1 == 0 or n == 1:
        return False

    m = n - 1
    s = 0
    while m & 1 == 0:
        m = m >> 1
        s += 1
    for i in range(iter_num):
        b = quick_pow(random.randint(2, n - 1), m, n)
        if b == 1 or b == n - 1:
            continue
        for j in range(s - 1):
            b = quick_pow(b, 2, n)
            if b == n - 1:
                break
        else:
            return False
    return True
def gcd(x, y):
    while (y):
        x, y = y, x % y
    return x

def is_prime(num):
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                    103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                    331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                    449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                    587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                    709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                    853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                    991, 997]
    for i in small_primes:
        if num%i==0:
            return False
    return millerRabinTest(num,5)

def get_prime(size):
    while True:
        num = random.randrange(1 << (size - 1), 1 << size)
        if is_prime(num):
            return num

def generate_private():
    p1 = get_prime(1023)
    while not is_prime(p1*2+1):
        p1=get_prime(1023)
    p=p1*2+1
    q = get_prime(1024)
    while gcd(p-1,q-1)!=2:
        q=get_prime(1024)
        print(gcd(p-1,q-1))
    return p,q


def generate_e(p,q):
    start=gmpy2.iroot(p*q,4)[0]
    d=get_prime(len(bin(start)))
    e=invmod(d,(p-1)*(q-1))
    while e<10000:
        d = get_prime(len(bin(start)))
        e = invmod(d, (p - 1) * (q - 1))
    return e,d



def main():
    p=int(input())
    q=int(input())
    e=int(input())
    m=int(input())
    op=int(input())
    if op==0:
        print(RSA_decrypt(p,q,e,m))
    elif op==1:
        print(RSA_encrypt(p,q,e,m))

if __name__ == '__main__':
    # p,q=generate_private()
    # #p=121299869147945018323914843433403543063328431957533702320613572931898280753261731983633842934605553108212051193567085120971107860708241377102448745203498106564234396438784764576708561018056373684152939023294465300639332668504453688330728772312206444163822799271683488379270913562543930302033837469744872756203
    # #q=107778788756397994704681429458950142943439895012713028247717943980622809154569235723622111687161416184680142777705659426265733698386592178595652557166219110422160142768635946465819648194478841299882168500506320300026349514949901292733592785523701086512241131629021465586010555734187369327466939968896393893779
    # e,d=generate_e(p,q)
    # print(p,q,d,e)
    main()