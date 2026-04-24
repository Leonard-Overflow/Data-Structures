"""
Um conjunto armazena todos 1 cópia de cada vaor que for passado para ele
- Não ordenada
- Mutável
- Sem duplicatas
- Sem index
"""

conjunto = {1, 2, 3, 4}
set = {3, 4, 5, 6}

# Inserindo no conjunto
lista = [8, 9]

# Vale para valores únicos e cojuntos de dados
conjunto.add(10)
conjunto.update(lista)
conjunto.update(set) # Nesse caso modiica o próprio conjunto e não cria um novo

# Removendo valores

conjunto.remove(10) # Lança erro se não existir
conjunto.discard(4) # Não lança erro se não existir
# Suporta o .pop e .clear

# Operando mais de um conjunto

# União de conjunto
conjunto.union(set)

# Intersecção de dois conjuntos
conjunto.intersection(set)

# Diferenças
conjunto.difference(set)
conjunto.symmetric_difference(set)

# Se _update(nome_do_conjunto) for colocado, modifica o conjunto que estiver chamando

# Verificações
conjunto.issubset(set) # Se está dento de set
conjunto.issuperset(set) # Se possui set
conjunto.isdisjoint(set) # Se não possuem elementos em comum
# Suporta o .copy


