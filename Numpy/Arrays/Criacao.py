import numpy as np

# Normal
array = np.array[0, 1, 2]

# So zeros tamebem tem apenas 1s com np.ones
zeros = np.zeros(3)

# Valor customizado
novo_array = np.full(3, 13)

# O np.empty reserva espaco na memoria, mas nao escreve nada.
# Se nao escrever os valores antes de ler podem acontecer problemas na execucao.

# Com parametro
np.array(3, dtype=float)

# _like em um array copia a forma

forma_principal = np.array((2, 4), dtype=int)
copia_da_forma = np.array_like(forma_principal,dtype=str)# Mesma forma, mas com "" no lugar de 0

