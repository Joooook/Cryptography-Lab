EXPECTED_LIST = [0.0804, 0.0148, 0.0334, 0.0382, 0.1249, 0.024, 0.0187, 0.0505, 0.0757, 0.0016, 0.0054, 0.0407, 0.0251,
                 0.0723, 0.0764, 0.0214, 0.0012, 0.0628, 0.0651, 0.0928, 0.0273, 0.0105, 0.0168, 0.0023, 0.0166, 0.0009]
ALPHA_SIZE = 26

def frequency_analysis(freq_list):
    diff_list = []
    for i in range(ALPHA_SIZE):
        tmp = []
        for j in range(ALPHA_SIZE):
            tmp.append((freq_list[i] - EXPECTED_LIST[j]) ** 2)
        diff_list.append(tmp)
    key_list=[]
    for i in diff_list:
        min=0
        for j in range(len(i)):
            if i[j]<i[min] :
                min=j
        key_list.append(min)
    key_list.sort()
    print(key_list)
    return ''

def the_test()


def score(freq_list):



if __name__ == '__main__':
    #EXPECTED_LIST.sort()
    freq_list = [0] * 26
    file = open("../test.txt", 'r')
    try:
        lines = file.readlines()
    finally:
        file.close()
    for i in lines:
        for j in range(ALPHA_SIZE):
            freq_list[j] += i.count(chr(j + ord('a')))
    sum = 0
    for i in freq_list:
        sum += i
    for i in range(len(freq_list)):
        freq_list[i] = freq_list[i] / sum
    frequency_analysis(freq_list)
