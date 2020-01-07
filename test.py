list = [2.9715, 1.1434, 0.7667, 0.5154]
sum_eigen = sum(list)
sum_ith = 0
for i in range(len(list)):
    sum_ith += list[i]
    ratio = sum_ith/sum_eigen
    print('sum to {0:d}th eigenvalues over sum of all eigenvalues:'.format(i+1), ratio)
    
