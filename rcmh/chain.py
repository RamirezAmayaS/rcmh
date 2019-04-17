import numpy
import random
import json
from math import trunc
from rcmh import config
from rcmh import transition
from rcmh import group

class Chain:

    def __init__(self,type,group):
        self.type = type
        self.group = group
        self.loss = transition.get_loss(group)
        self.best = {'loss':self.loss,'grouping':self.group.grouping}

    def step(self,i,poisson_lambda):
        with open("/Users/RamirezAmayaS/clustering/platinum/optimal_30.csv", "a") as outfile:
            if self.type == 'poisson':
                distance = numpy.random.poisson(poisson_lambda)
                print(f'Se considera candidato a un distancia de {distance}')
                group_candidate = group.Group(self.group.codes,self.group.groups,self.group.reassign(distance))
                #loss_candidate = transition.get_loss(self.group)
                loss_candidate = transition.get_loss(group_candidate)
                print(f'La pérdida del candidato es {trunc(loss_candidate)} \n')
                alpha = transition.get_alpha(self.loss,loss_candidate,config.temperature)
                print(f'Alpha tiene un valor de {str(alpha)} \n')
                decision = random.random() < alpha
                if decision:
                    print(f'Se acepta candidato! \n')
                    self.loss = loss_candidate
                    self.group = group_candidate
                    if self.loss < self.best['loss']:
                        self.best = {'loss':self.loss,'grouping':self.group.grouping}
                        with open("/Users/RamirezAmayaS/clustering/platinum/optimal_30.csv", "w") as outfile_opt:
                            outfile_opt.write(json.dumps(self.best))
                else:
                    print(f'Se rechaza candidato! \n')

                print(f"Mejor MAE es {trunc(self.best['loss'])} \n")

                outfile.write(f"{i},{poisson_lambda},{distance},{loss_candidate},{alpha},{decision},{self.best['loss']}\n")

    def walk(self,steps,poisson_lambda):
        print('Iniciando caminata... \n')
        i = 0
        while i < steps:
            print('\n')
            print('*********************************************************************************')
            print(f'Iniciando iteración {i}.. \n')
            print(f'La pérdida actual es {trunc(self.loss)} \n')
            self.step(i,poisson_lambda)
            print('*********************************************************************************')
            i = i + 1

    def walks(self,steps):
        for poisson_lambda in config.poisson_lambda:
            self.walk(steps,poisson_lambda)
