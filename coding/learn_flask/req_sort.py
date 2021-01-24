# -*- coding: utf-8 -*-


with open('requirements.txt', 'r') as f:
    req = []
    for line in f:
        print(line)
        req.append(line)

req.sort(key=lambda x: x.lower())

print('-'*30)

with open('requirements.txt', 'w') as f:

    for package in req:
        print(package)
        f.write(package)
