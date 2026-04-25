"""Series são basicamente arrays unidimensionais podendo possuir vários tipos de dados"""

import pandas as pd

serie = pd.Series([1, True, "texto", 3.14], [0, 1, 2, 3])
int_serie = pd.Series([1, 2, 3,4 ,5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9])
char_serie = pd.Series(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
float_serie = pd.Series([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
bool_serie = pd.Series([True, False], [1, 0])

# Métodos sobre os atrributos da serie

# Vendo os tipos de dados de uma  serie
dados = int_serie.dtype # Ou dtypes, mas este é para Data Frames

# Vendo os indexes
index = char_serie.index

# Vendo o vaor de cada item do array
valores = serie.values
print(valores)
