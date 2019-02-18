import math
import scipy
import pandas as pd
from rcmh import config

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
    alpha = min(1,pi_candidate/pi_actual)
    return alpha

def get_loss(group):
    train_sample_x, train_sample_y = get_sample(group)
    test_sample_x, test_sample_y = get_sample(group)
    regr = linear_model.LinearRegression()
    regr.fit(train_sample_x,train_sample_y)
    test_hat_y = regr.predict(test_sample_x)
    mae = -1*mean_absolute_error(test_hat_y,test_sample_y)
    return mae

def get_features_from_diag(sample,group):
    df = pd.DataFrame(0,index=sample.index,columns=group.groups)
    for column in config.diag_columns:
        df.loc[sample[column]==1,group.grouping[column]] = 1
    return df

def get_sample(group):
    sample = config.diag_csv.sample(1*10^5))
    sample_x = pd.concat([sample[config.feature_columns],get_features_from_diag(sample,group)],axis=1)
    sample_y = sample[config.target_columns]
    return sample_x,sample_y
