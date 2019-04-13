import sys
a = int(sys.argv[1]) #works only for positive values
b = int(sys.argv[2])
product = 0
while a!=1:
    if (a%2)!=0:
        product = product+b
    a = a//2
    b = b*2
product = product+b
print(product)
    
