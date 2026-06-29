import numpy as np

dtype_proprio = np.dtype([
    ('nome', 'U15'),
    ('departamento', 'U20'),
    ('idade', np.int8),
    ('salario', np.float32),
    ('status', np.bool)
])

funcionarios = np.array([
    ("Leonardo", "Dados", 19, 3200.0, True),
    ("Rafael", "RH", 26, 3500.0, True),
    ("Francisco", "Dados", 29, 4000.0, True),
    ("Leonardo", "Marketing", 23, 3000.0, False),
], dtype_proprio)

# Por indice
print(funcionarios[0])

# Por "coluna"
print(funcionarios["idade"])

# Cruzando os dois
print(funcionarios[3]["salario"])