Key_Substitution_1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
                      10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
                      63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
                      14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
Key_Substitution_2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
                      23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
                      41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
                      44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
key_shift = [0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
Extension = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,
             8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
             16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
             24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
IP_Sub = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
IP_Inv = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
PBox = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
SBox_1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
          0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
          4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
          15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
SBox_2 = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
          3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
          0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
          13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
SBox_3 = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
          13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
          13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
          1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
SBox_4 = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
          13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
          10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
          3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
SBox_5 = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
          14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
          4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
          11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
SBox_6 = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
          10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
          9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
          4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
SBox_7 = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
          13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
          1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
          6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
SBox_8 = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
          1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
          7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
          2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
SBox = [SBox_1, SBox_2, SBox_3, SBox_4, SBox_5, SBox_6, SBox_7, SBox_8]


def generate_subkey(key):
    sub1 = ""
    for i in range(56):
        sub1 = sub1 + key[Key_Substitution_1[i] - 1]
    c = sub1[0:28]
    d = sub1[28:56]
    key_sublist = []
    for i in range(16):
        c = c[key_shift[i + 1]:] + c[:key_shift[i + 1]]
        d = d[key_shift[i + 1]:] + d[:key_shift[i + 1]]
        sub2 = ""
        temp = c + d
        for j in range(48):
            sub2 = sub2 + temp[Key_Substitution_2[j] - 1]
        key_sublist.append(sub2)
    return key_sublist


def S_Substitution(s):
    s_list = ['' for _ in range(8)]
    for i in range(8):
        s_list[i] = s[i * 6:(i + 1) * 6]
    ans = ""
    for i in range(8):
        row = int(s_list[i][0] + s_list[i][5], 2)
        column = int(s_list[i][1:5], 2)
        ans = ans + bin(SBox[i][row * 16 + column])[2:].rjust(4, '0')
    return ans


def encryption(msg, key):
    msg = bin(int(msg, 16))[2:].rjust(64, '0')
    msg_sub = ""
    for i in range(64):
        msg_sub = msg_sub + msg[IP_Sub[i] - 1]

    Li = msg_sub[0:32]
    Ri = msg_sub[32:64]
    for i in range(16):
        temp_L = Li
        Li = Ri
        ex_R = ""
        for j in range(48):
            ex_R = ex_R + Ri[Extension[j] - 1]
        temp = bin(int(ex_R, 2) ^ int(key[i], 2))[2:].rjust(48, '0')
        temp_depress = S_Substitution(temp)
        temp_sub = ""
        for j in range(32):
            temp_sub = temp_sub + temp_depress[PBox[j] - 1]
        Ri = bin(int(temp_L, 2) ^ int(temp_sub, 2))[2:].rjust(32, '0')

    cipher_tmp = Ri + Li
    cipher = ""
    for i in range(64):
        cipher = cipher + cipher_tmp[IP_Inv[i] - 1]
    return '0x' + hex(int(cipher, 2))[2:].rjust(16, '0')


def decryption(cipher, key):
    cipher = bin(int(cipher, 16))[2:].rjust(64, '0')
    cipher_sub = ""
    for i in range(64):
        cipher_sub = cipher_sub + cipher[IP_Sub[i] - 1]

    Li = cipher_sub[0:32]
    Ri = cipher_sub[32:64]
    for i in range(15, -1, -1):
        temp_L = Li
        Li = Ri
        ex_R = ""
        for j in range(48):
            ex_R = ex_R + Ri[Extension[j] - 1]
        temp = bin(int(ex_R, 2) ^ int(key[i], 2))[2:].rjust(48, '0')
        temp_depress = S_Substitution(temp)
        temp_sub = ""
        for j in range(32):
            temp_sub = temp_sub + temp_depress[PBox[j] - 1]
        Ri = bin(int(temp_L, 2) ^ int(temp_sub, 2))[2:].rjust(32, '0')

    msg_tmp = Ri + Li
    msg = ""
    for i in range(64):
        msg = msg + msg_tmp[IP_Inv[i] - 1]
    return '0x' + hex(int(msg, 2))[2:].rjust(16, '0')


def EDE(k1, k2, x):
    s = encryption(x, k1)
    s = decryption(s, k2)
    s = encryption(s, k1)
    return s


def xor(x, y):
    x = int(x, 16)
    y = int(y, 16)
    ans = hex(x ^ y)[2:].rjust(16, '0')
    return '0x' + ans


def main():
    iv = input().strip().replace('\n', '').replace('\r', '')
    k1 = input().strip().replace('\n', '').replace('\r', '')
    k2 = input().strip().replace('\n', '').replace('\r', '')
    num = int(input())
    t = []
    k1 = bin(int(k1, 16))[2:].rjust(64, '0')
    k2 = bin(int(k2, 16))[2:].rjust(64, '0')
    key_list_1 = generate_subkey(k1)
    key_list_2 = generate_subkey(k2)
    for i in range(num):
        t.append(input().strip().replace('\n', '').replace('\r', ''))
    for i in range(num):
        r = EDE(key_list_1, key_list_2, xor(iv, EDE(key_list_1, key_list_2, t[i])))
        iv = EDE(key_list_1, key_list_2, xor(r, EDE(key_list_1, key_list_2, t[i])))
        print(r)


if __name__ == '__main__':
    main()