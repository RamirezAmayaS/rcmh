import math
import scipy
import pandas as pd
from rcmh import config
from sklearn import linear_model
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import cross_val_score

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
    print('loss_actual',loss_actual)
    print('loss_candidate',loss_candidate)
    pi_actual = math.exp(-1*(loss_actual-710000)/t)
    print('pi_actual',pi_actual)
    pi_candidate = math.exp(-1*(loss_candidate-710000)/t)
    print('pi_candidate',pi_candidate)
    print('div',pi_candidate/pi_actual)
    alpha = min(1,pi_candidate/pi_actual)
    return alpha

def get_loss(group):
    train_sample_x, train_sample_y = get_sample(group,'train')
    test_sample_x, test_sample_y = get_sample(group,'test')
    regr = linear_model.LinearRegression(n_jobs=4)
    regr.fit(train_sample_x,train_sample_y)
    test_hat_y = regr.predict(test_sample_x)
    mae = mean_absolute_error(test_hat_y,test_sample_y)
    return mae

def get_loss_upper(group):
    train_sample_x, train_sample_y = get_sample(group,'train')
    test_sample_x, test_sample_y = get_sample(group,'test_upper')
    regr = linear_model.LinearRegression()
    regr.fit(train_sample_x,train_sample_y)
    test_hat_y = regr.predict(test_sample_x)
    mae = mean_absolute_error(test_hat_y,test_sample_y)
    return mae

def get_loss_lower(group):
    train_sample_x, train_sample_y = get_sample(group,'train')
    test_sample_x, test_sample_y = get_sample(group,'test_lower')
    regr = linear_model.LinearRegression()
    regr.fit(train_sample_x,train_sample_y)
    test_hat_y = regr.predict(test_sample_x)
    mae = mean_absolute_error(test_hat_y,test_sample_y)
    return mae

def get_features_from_diag(sample,group):
    #df = pd.DataFrame(0,index=sample.index,columns=group.groups)
    #for column in config.diag_columns:
    #    df.loc[sample[column]==1,group.grouping[column]] = 1
    #return df
    a = sample[config.diag_columns].groupby(by=group.grouping,axis=1)
    return a.any()

def get_sample(group,type):
    #sample = config.diag_csv.sample(config.sample_size)
    if type == 'train':
        sample = config.train
    elif type == 'test_upper':
        sample = config.test[config.test['VALOR_TOT_2011'] >= config.test['VALOR_TOT_2011'].quantile(q=0.90)]
    elif type == 'test_lower':
        sample = config.test[config.test['VALOR_TOT_2011'] <= config.test['VALOR_TOT_2011'].quantile(q=0.10)]
    else:
        sample = config.test
    #sample_x = pd.concat([sample[config.feature_columns],get_features_from_diag(sample,group)],axis=1)
    sample_x = sample[config.feature_columns]
    sample_y = sample[config.target_columns]
    return sample_x,sample_y

def get_loss_cv(group):
    train_sample_x, train_sample_y = get_sample(group,'train')
    test_sample_x, test_sample_y = get_sample(group,'test')
    regr = linear_model.LinearRegression(n_jobs=4)
    #regr.fit(train_sample_x,train_sample_y)
    #test_hat_y = regr.predict(test_sample_x)
    #mae = mean_absolute_error(test_hat_y,test_sample_y)
    mae = cross_val_score(estimator=regr,X=train_sample_x,y=train_sample_y,cv=5,scoring='neg_mean_absolute_error')
    return mae

def get_loss_upper_cv(group):
    train_sample_x, train_sample_y = get_sample(group,'train')
    test_sample_x, test_sample_y = get_sample(group,'test_upper')
    regr = linear_model.LinearRegression()
    regr.fit(train_sample_x,train_sample_y)
    test_hat_y = regr.predict(test_sample_x)
    mae = mean_absolute_error(test_hat_y,test_sample_y)
    return mae

def get_loss_lower_cv(group):
    train_sample_x, train_sample_y = get_sample(group,'train')
    test_sample_x, test_sample_y = get_sample(group,'test_lower')
    regr = linear_model.LinearRegression()
    regr.fit(train_sample_x,train_sample_y)
    test_hat_y = regr.predict(test_sample_x)
    mae = mean_absolute_error(test_hat_y,test_sample_y)
    return mae
