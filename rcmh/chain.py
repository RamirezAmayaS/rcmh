import numpy
from rcmh import config
from rcmh import transition

class Chain:

    def __init__(self,type,group,loss):
        self.type = type
        self.group = group
        self.loss = transition.get_loss(group)

    def step(self):
        if self.type == 'poisson':
            distance = numpy.random.poisson(config.poisson_lambda)
            group_candidate = self.group.reassign(distance)
            loss_candidate = transition.get_loss(group_candidate)
            alpha = transition.get_alpha(self.loss,loss_candidate,config.temperature)
            if random.random() < alpha:
                self.group = candidate_group
                self.loss = loss_candidate

    def walk(self,steps):
        i = 0
        while i < steps:
            self.step()
