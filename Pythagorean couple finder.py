import math as m
z = lambda x, y: x**2 + y ** 2

k = 0
for i in range (1, 100):
    for j in range(i, 100):
        p = z(i, j)
        n = m.sqrt(p)
        if m.fabs(n-m.floor(n)) < .001 :
            k += 1
            print(i, j, m.floor(n))
print('Number of pythogerean couples =',k)
