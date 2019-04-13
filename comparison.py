import sys

a =int(sys.argv[1])
b =int(sys.argv[2])

greater=((a+b)+abs(a-b))//2
lesser = ((a+b)- abs(a-b))//2
print("the greater value is:",greater)
print("the lesser value is:",lesser)
