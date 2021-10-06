 
def check(x):
 #    for i in range(2, int(x**0.5)+2): #16**0.5  = 3,999999
 #        if x % i == 0:
 #            return False
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i = i + 1
    
    return True

r_max = 3_532_160
r = [True] * (r_max+1)
r[0] = r[1] = False

for i in range(2, r_max):
    if r[i]:
        for j in range(i*i, r_max + 1, i):
           r[j] = False

#print(r)
a = 150_505
b = 174_505

for i in range(a, b+1):
    if round(i**0.5)**2==i:
       if r[round(i**0.5)]:
           print(i)


for i in range(int(a**0.5), int(b**0.5)+2):
    if r[i] and a<=i*i<=b:
           print(i*i)
