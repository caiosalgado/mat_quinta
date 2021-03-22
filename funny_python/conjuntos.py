# descubra engenheiros que nao sao gerentes

engenheiros = {'bob', 'sue', 'ann', 'vic'}
gerentes = {'tom', 'sue'}

print(engenheiros.difference(gerentes))

# bob e sue são engenheiros?

testar = {'bob', 'sue'}

print(testar.issubset(engenheiros))

# descubra os elementos em comum

print(engenheiros.intersection(gerentes))

print(engenheiros & gerentes)

# todas as pessoas nos conjuntos abaixo

print(engenheiros.union(gerentes))

# todos os gerentes sao engenheiros?

print(gerentes.issubset(engenheiros))

# Bunch

class Bunch:
    """Bunch é um dicionario que suporta acesso ao atributo
       a la js"""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


empregado = Bunch(name='caio', position='coder')
empregado.name
empregado.position

# engenheiros que nao sao gerentes

engenheiros.difference(gerentes)
testar.issubset(engenheiros)