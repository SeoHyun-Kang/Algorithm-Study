#import random

height = []
#rand_h = []
s = 0

for i in range(9):
    height.append(int(input()))
    s += height[i]

height.sort() 

for i in range(9):
    for j in range(i+1, 9):
        if (s - height[i] - height[j]) == 100:
            for k in range (9):
                if k == i or k==j:
                    continue
                else:
                    print(height[k]) 


'''
while True:
    rand_h = random.sample(height,7)
    s = sum(rand_h)
    if sum == 100:
        break
rand_h.sort()

for i in range(7):
    print(rand_h[i])
'''




