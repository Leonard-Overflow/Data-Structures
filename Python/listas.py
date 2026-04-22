"""
Uma lista é uma série de elementos e possui as seguintes caracteristicas:
- Mutavel
- Ordenanda
- Indexada
- Permite duplicatas
- E aceita vários tipos
"""

lista = [] # inicialmente vazia

# Add clientes
lista.append("Joao")
lista.append("Maria")
lista.append("Rafael")

# Inserindo em uma posição específica
lista.insert(2, "Pedro")

# Adiconando elementos de outra lista
lista_add = ["Kaua", "Giovana"]
lista.extend(lista_add)

# Removendo um item
lista.remove("Kaua")

# Removendo e guardando um item
nome = lista.pop(4)
print(nome)

# Pegando o index de um item
print(lista.index("Rafael"))

# Contando elementos

# Mais elementos para a contagem
lista.append("Rafael")
lista.append("Rafael")
print(lista.count("Rafael"))

# Ordenando(por ordem alfabética no caso)
print(lista.sort)
# O algoritmo usado no .sort do python é o timesort

# Invertendo a lista
lista.reverse()

# Copiando para outra lista

lista_2 = lista.copy()

# Apagando toda a lista
lista.clear()