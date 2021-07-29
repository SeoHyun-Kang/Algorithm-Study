n = int(input())
lst = []

for i in range(n):
    l = list(map(int,input().split()))
    l.sort()
    lst.append(l)
    

for j in range(n):
    print(lst[j][7])

'''
x = int(input())
for i in range(x):
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums[-3])
'''