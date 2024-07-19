import pandas as pd

# 1- Importando dados
data = pd.read_excel("data/VendaCarros.xlsx")
print(data)

# 2- Lista os primeiros regitros
print(data.head())

# 3- Lista os útilmos registros
print(data.tail())

# 4- Contagem de valores por Fabricante
print(data["Fabricante"].value_counts())
