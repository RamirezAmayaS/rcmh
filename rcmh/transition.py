import math
import scipy

def count_partitions(n,d,k):
    nCd =  math.factorial(n)/(math.factorial(d)*math.factorial(n-d))
    return nCd*(k-1)**d

def get_uniform_transition_prob(n,d,k):
    count = 0
    for j in range(0,d+1):
        count += count_partitions(n,d,k)
    prob = 1/count
    return prob

def get_poisson_transition_prob(n,d,k,j):
    poisson = scipy.stats.poisson(j).pmf(d)
    count = count_partitions(n,d,k)
    prob = (1/count)*poisson
    return prob

def get_alpha(loss_actual,loss_candidate,t):
    pi_actual = math.exp(-1*loss_actual/t)
    pi_candidate = math.exp(-1*loss_candidate/t)
    alpha = pi_candidate/pi_actual
    return alpha 
