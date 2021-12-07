 
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
a = 3_532_000
b = 3_532_160

for i in range(a, b+1):
#    if check(i):
    if r[i]:
        print(i)


