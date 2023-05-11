import random
import hashlib
def main():
    n=int(input())//4
    m=input()
    s=''
    for i in range(1<<50):
        s=str(i)
        if hashlib.sha1(s.encode()).hexdigest()[:n]==m[:n]:
            break
    print(s)
if __name__ == '__main__':
    main()