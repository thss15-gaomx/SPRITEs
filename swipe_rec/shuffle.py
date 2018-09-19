import random

f = open('train.txt')
txt = []
for line in f:
    txt.append(line.strip())

random.shuffle(txt)

for item in txt:
    print(item)