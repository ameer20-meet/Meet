import math
def ok():
    a = [1,234,33,4,42,3432,42,32,4]
    b = [a[0],a[-1]]
print (ok())

a = [1,234,33,4,42,3432,42,32,4]
E = [1,2341,33,4,42,3432,42,321]
C = []
for i in a:
    if i not in C and i in E:
        C.append(i)

print (C)


input1= int(input("prime or nah?"))
for i in range(int(math.sqrt(input1))):
    if(input1%(i+1) == 1):
        print("not prime")
