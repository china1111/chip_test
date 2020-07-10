import json

dic = {}
with open("123.txt", 'r') as f1:
    for i in f1:
        if i == '':
            continue
        i = i.strip().split()
        dic[i[1]] = i[0]

print(dic)
with open('statuscode.json', 'w') as f1:
    json.dump(dic, f1)
