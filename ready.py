import json
dic = {}
with open("配置值.txt", 'r') as f1:
    for i in f1:
        i = i.strip().split()
        if i == []:
            continue
        dic[i[0]] = i[1:]

with open("level.json", 'w') as f2:
    json.dump(dic, f2)
