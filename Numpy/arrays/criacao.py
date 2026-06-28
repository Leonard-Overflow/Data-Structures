import numpy as np

# Normal
array = np.array([0, 1, 2])

# So zeros tamebem tem apenas 1s com np.ones
zeros = np.zeros(3)

# Valor customizado
novo_array = np.full(3, 13)

# O np.empty reserva espaco na memoria, mas nao escreve nada.
# Se nao escrever os valores antes de ler podem acontecer problemas na execucao.

# Com parametro
parametro = np.array((1, 2, 3, 4), dtype=int)

# _like em um array copia a forma

forma_principal = np.array((2, 4), dtype=int)
copia_da_forma = np.full_like(forma_principal, "", dtype=str)# Mesma forma, mas com "" no lugar de 0

print(parametro)