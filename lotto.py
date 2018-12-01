import random
num = []
result = []

for i in range(1,46):
    num.append(i)
    
for i in range(1,7):
    lotto = random.choice(num)
    result.append(lotto)
    num.remove(lotto)

result.sort()
for k in result:
    print(k, end = '\t')