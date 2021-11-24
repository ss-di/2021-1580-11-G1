 
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
a = 77_777_777
b = 88_888_888

ans = []
x = 3
while x**4<=b:
    if r[x]:
        y = x**4
        while y <=b:
            if y>=a:
                print(y, x)
                ans.append((y, x))
            y *= 2
    x+=2            

ans.sort()
print(ans)
