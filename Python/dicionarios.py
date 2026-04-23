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

# Atualizando dados
Paises.update({"Brasil" : "Rio de Janeiro"})

# Inserindo novos dados
Paises.setdefault("Brasil", "Sao Paulo") # Não insere, pois já existe um valor ligado a Brasil
Paises.setdefault("Japao", "Toquio") # Funciona, pois não  existe uma chave Japao

# Possui o .pop(com default) e clear

# Removendo e guardando um par
pais = Paises.popitem()
print(pais)

# Copiando os valores
Nacoes = Paises.copy()

# Copiando uma parte
Estados = Paises.fromkeys(["Brasil", "China"], ["Sao Paulo", "Shanghai"]) # um novo dicionário com Brasil e China com os valores sendo Sao Paulo para Brasil e Shanghai para China

