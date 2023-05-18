def max_freq(s):
    freqList=[0]*26
    max=0
    for i in s:
        freqList[ord(i)-ord('a')]+=1
    for i in range(len(freqList)):
        if freqList[i]>freqList[max]:
            max=i
    return chr(max+ord('a'))

def main():
    s=input().strip()
    print((ord(max_freq(s))-ord('e'))%26)