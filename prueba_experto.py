from rcmh import config,group,chain,expert 

grupo_inicial = expert.construct_expert_extended_group()
cadena = chain.Chain(type='poisson',group=grupo_inicial)
cadena.walks(1000)
