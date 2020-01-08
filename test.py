list = [1030.8, 574.4, 67.7, 19.2, 14.3, 6.0, 2.5, 1.9, 0.6, 0.5]
sum_eigen = sum(list)
sum_ith = 0
for i in range(len(list)):
    sum_ith += list[i]
    ratio = sum_ith/sum_eigen
    print('sum to {0:d}th eigenvalues over sum of all eigenvalues:'.format(i+1), ratio)
    
