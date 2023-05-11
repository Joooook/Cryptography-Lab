import hashlib
import random
import re
import string
MSG="这是一段针对SHA1的第二类生日攻击，虽然两句话很像，但SHA1值前32bit相同"
PAD_LEN=20
COD_LEN=8
PAD_CHARS=" "
if __name__ == '__main__':
    dic = {}
    while True:
        msg_list = re.findall(r'.{1}', MSG)
        for _ in range(PAD_LEN):
            index=random.randint(0,len(msg_list))
            msg_list.insert(index,random.choice(PAD_CHARS))
        pad_msg=''.join(msg_list)
        hash_value=hashlib.sha1(pad_msg.encode()).hexdigest()[:COD_LEN]
        if hash_value in dic and pad_msg!=dic[hash_value]:
            print(pad_msg)
            print(hashlib.sha1(pad_msg.encode()).hexdigest())
            print(dic[hash_value])
            print(hashlib.sha1(dic[hash_value].encode()).hexdigest())
            break
        dic[hash_value] = pad_msg



