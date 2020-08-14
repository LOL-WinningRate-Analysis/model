import json

a = []
with open('.\data\datas.txt', 'r') as f:
    a = f.read()
i = 0
while a[i] != '>':
    if a[i] == '}':
        if a[i+1] != ',':
            a = a[:i+1] + ',' + a[i+1:]
    i = i + 1
print("fix done")
with open('.\data\datas2.txt', 'w') as f:
    f.write(a)
