P = int(input())
E = 0.0000000000001
a = 1
b = P

c = abs(a - b)

while c > E:
    a = (a+b)/2
    b = P/a
    c = abs(a - b)

print(b)