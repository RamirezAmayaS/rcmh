import math
import scipy

def count_partitions(n,d,k):
    nCd =  math.factorial(n)/(math.factorial(d)*math.factorial(n-d))
    return nCd*(k-1)**d

def uniform_distribution(n,d,k):
    count = 0
    for j in range(0,d+1):
        count += count_partitions(n,d,k)
    prob = 1/count
    return prob

def poisson_distribution(n,d,k,j):
    poisson = scipy.stats.poisson(j).pmf(d)
    count = count_partitions(n,d,k)
    prob = (1/count)*poisson
    return prob
