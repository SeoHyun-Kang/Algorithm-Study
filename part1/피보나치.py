def fb(n):
    if n<=1:
        return n
    return fb(n-1)+fb(n-2)

n = int(input())
print(fb(n))

    