from rcmh import config,group,chain 
grupo_inicial = group.Group(config.diag_columns,config.groups,None)
cadena = chain.Chain(type='poisson',group=grupo_inicial)
cadena.walks(100)
