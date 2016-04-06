i=1
while(i<10):
    for j in range(i, 10):
        formula = '{0:1}x{1:1}={2:<2}'.format(i, j, i*j)
        print(formula, end=' ')
    i+=1 
    print()