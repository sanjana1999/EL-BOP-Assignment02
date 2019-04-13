"""
d= sum((-1^k)(r!/k!))from 0 to r
here p= r!/k!   p=5;5*4;5*4*3...
at k=0  p = 5*4*3*2*1
"""
import sys
r = int (sys.argv[1])
d = 0
p = 1

for i in range (r,-1,-1):     #i= 5,4,3,2,1,0
    if  i!=0:
        d = d+(((-1)**i)*p)   
        p = p*i
    else:
        d = d+p
print ("no of ways", r ,"can be arranged such that its not in original place is",d)

