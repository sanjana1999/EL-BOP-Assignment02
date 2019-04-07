sum = 1;
x = int(input(""))
no_of_term = int(input(""))
term = 1
for i in range (1,no_of_term):
    term = term*i
    sum = sum + ((x**i)/term)
print (sum)
