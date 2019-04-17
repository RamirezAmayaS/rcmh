from rcmh import group
from rcmh import transition
from rcmh import config

import json


def estimate_expert_loss():
    expert_group = construct_expert_group()
    loss_expert = transition.get_loss_cv(expert_group)
    return loss_expert

def estimate_expert_loss_upper():
    expert_group = construct_expert_group()
    loss_expert = transition.get_loss_upper_cv(expert_group)
    return loss_expert

def estimate_expert_loss_lower():
    expert_group = construct_expert_group()
    loss_expert = transition.get_loss_lower_cv(expert_group)
    return loss_expert

def estimate_mh_loss():
    mh_group = construct_mh_group()
    loss_mh = transition.get_loss_cv(mh_group)
    return loss_mh

def estimate_mh_loss_upper():
    mh_group = construct_mh_group()
    loss_mh = transition.get_loss_upper_cv(mh_group)
    return loss_mh

def estimate_mh_loss_lower():
    mh_group = construct_mh_group()
    loss_mh = transition.get_loss_lower_cv(mh_group)
    return loss_mh

def construct_expert_group():
    codes = config.diag_columns
    groups = ['0','1']
    expert_grouping = {code:'0' for code in codes}
    for code in config.expert:
        expert_grouping[code] = '1'
    return group.Group(codes,groups,expert_grouping)

def construct_expert_extended_group():
    codes = config.diag_columns
    groups = [str(x) for x in list(range(30))]
    return group.Group(codes,groups,config.expert_30)

def construct_mh_group():
    codes = config.diag_columns
    groups = [str(x) for x in range(96)]
    with open('/Users/RamirezAmayaS/clustering/finales/optimal_30_estasi_2.csv') as infile:
        mh_group = json.load(infile)['grouping']
    return group.Group(codes,groups,mh_group)
