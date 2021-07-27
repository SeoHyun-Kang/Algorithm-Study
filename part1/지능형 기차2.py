passenger = 0
n = []

for _ in range (10):
    a, b = map(int, input().split())
    passenger -= a
    passenger += b
    n.append(passenger)

print(max(n))

