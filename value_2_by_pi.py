product = (1/2)**(1/2)
x = 2**(1/2)
no_of_terms = int(input(""))
for i in range (1,no_of_terms):
    x = (2+x)**(1/2)
    product = product*(x/2)
print( product )
