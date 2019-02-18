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
            print(f'Se considera candidato a un distancia de {distance}')
            group_candidate = self.group.reassign(distance)
            loss_candidate = transition.get_loss(group_candidate)
            print(f'La pérdida del candidato es {loss_candidate} \n')
            alpha = transition.get_alpha(self.loss,loss_candidate,config.temperature)
            if random.random() < alpha:
                print(f'Se acepta candidato! \n')
                self.group = candidate_group
                self.loss = loss_candidate
            else:
                print(f'Se rechaza candidato! \n')

    def walk(self,steps):
        print('Iniciando caminata... \n')
        i = 0
        while i < steps:
            print('\n')
            print(f'Iniciando iteración {i}.. \n')
            print(f'La pérdida actual es {self.loss} \n')
            self.step()
