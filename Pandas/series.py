import pandas as pd

"""As series são basicamente arrays, mas com pequenos adicionais que permitem certas interações com outras estruturas"""

# Crinado uma serie

# Jeito direto
serie = pd.Series(values = ("a", "b", "c", "d"), index = (1, 2, 3, 4))

# A partir de uma lista ou tupla
lista = ["a", "b", "c", "d"]
tupla = (1, 2, 3)

serie_list = pd.Series(lista)
serie_tupla = pd.Series(tupla)

# Também é possível com sets, mas a ordem pode acabar variando a cada execução

# É possível fazer o mesmo com um dicionário, mas nesse caso as chaves viram os indices

dict = {
    1 : "a",
    2 : "b",
    3 : "c",
    4 : "d"
}

serie_dict = pd.Series(dict)

# Repetindo um valor para todas as colunas

colunas = pd.Series(values = 7, index = [1, 2, 3, 4])

# Series permitem operações de fatiamento, filtro, operações matemáticas

# Os métodos próprios de uma serie são

# Para acesso
serie.get(2, 0) # Retorna 0 se não encontrar
#serie["2"] Retorna erro se não encontrar

# Em relação aos nulos
serie.isnull() # Retorna True para todos os nulos que encontrar
serie.notnull() # Retona False pata todos os nulos que encontrar
serie.fillna(0) # Substitui os nullos pelo valor passado. Pode ser usado com methods como ffill(substitui pelo anterior), bfill(substitui pelo posterior), etc

# Estatístisca
serie.mean()
serie.sum()
serie.describe() # Devolve um resumo da serie, quantos elementos, maior elemento, média, etc
serie.count()
# etc

# Atrtibutos utéis
serie.values()
serie.index()
dtype = serie.dtype
shape = serie.shape
name = serie.name