import sys

x = int(sys.argv[1])
no_term = int(sys.argv[2])
sum = 1
term = 1
for i in range (1,no_term):
    term = (term*x)/i
    sum = sum + term
print (sum)
