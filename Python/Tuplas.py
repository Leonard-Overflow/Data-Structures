"""
Uma tupla é uma série de elementos e possui as seguintes caracteristicas:
- Imutavel
- Ordenanda
- Indexada
- Permite duplicatas
- E aceita vários tipos
- Pode servir como chave de um dicionário(se os elementos também forem chaves de dicionários)
"""

tupla = (1, 1, 1, 1, 2)

# Pegando um elemento pelo index
print(tupla.index(0))

# Contando elementos
tupla.count(1)

# Como um tupla é imutável então é possível faze-la chave de um dicionário
coordenadas = {}

coordenada_casa = (5, 10)
coordenada_trabalho = (10, 15)

coordenadas[coordenada_casa] = "Casa"
coordenadas[coordenada_trabalho] = "Trabalho"