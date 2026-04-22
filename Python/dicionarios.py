"""
Dicionários(ou hashmaps) são estruturas que possuem uma chave e um valor correspondentes. A chave
deve ser imutável, mas seu valor pode ser alterado. Um dicionário possui as seguintes caracteristicas:
- Cada elemento é um par chave-valor
- Mutável
- Não permite chaves duplicadas ou mutáveis
- Acesso única e exclusivamente por chaves
"""

Paises = {
    "Brasil" : "Brasilia",
    "Estados Unidos" : "Washington",
    "China" : "Beijing"
}

# Pegando um valor qualquer
Paises.get("Brasil", "Nao existe")
# Retorna "Nao existe" se não houver

# Vendo todas as chaves
print(Paises.keys())

# Vendo todos os valores
print(Paises.values())

# Vendo todos os pares
print(Paises.items())