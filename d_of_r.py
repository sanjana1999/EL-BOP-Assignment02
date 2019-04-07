r = int (input (""))
d = 0
p = 1

for i in range (r,-1,-1):
    if  i!=0:
        d = d+(((-1)**i)*p)
        p = p*i
    else:
        d = d+p
print (d)

