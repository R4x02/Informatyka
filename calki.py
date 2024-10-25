def funkcja(x):
    return x*x+1

def calki(a, b, E = 1000):
    x = (b-a)/E
    pole = 0
    for i in range(E):
        y = funkcja(a+i*x)
        pole += y*x
    return pole

print(calki(1,3))