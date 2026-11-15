# Exercício 6 — Matriz de distâncias entre registros
import math

import pandas as pd

registros = {
    "A": [1, 1],
    "B": [4, 5],
    "C": [2, 2],
    "D": [5, 4],
}

nomes = list(registros.keys())

# 28. Calcular a distância entre todos os pares com math.dist()
# 29. Montar a matriz de distâncias com pandas.DataFrame
matriz = pd.DataFrame(index=nomes, columns=nomes, dtype=float)
for i in nomes:
    for j in nomes:
        matriz.loc[i, j] = math.dist(registros[i], registros[j])

print("Matriz de distâncias:")
print(matriz.round(4))

# 30 e 31. Menor valor diferente de zero e o par mais próximo
# Percorre só a metade superior da matriz (i < j) para não repetir pares.
pares = []
for a in range(len(nomes)):
    for b in range(a + 1, len(nomes)):
        valor = matriz.iloc[a, b]
        if valor != 0:
            pares.append((valor, nomes[a], nomes[b]))

menor = min(p[0] for p in pares)
# Pode haver empate: lista todos os pares com a menor distância.
mais_proximos = [(i, j) for v, i, j in pares if math.isclose(v, menor)]

print(f"\nMenor distância diferente de zero: {menor:.4f}")
for i, j in mais_proximos:
    print(f"Par de registros mais próximo: {i} e {j}")

# 32. Verificar que a diagonal principal possui apenas zeros
# A diagonal compara cada registro com ele mesmo: todas as diferenças entre os
# atributos são zero, então a soma dos quadrados é zero e d(X, X) = 0.
diagonal_zero = all(matriz.loc[n, n] == 0 for n in nomes)
print(f"\nDiagonal principal só tem zeros? {diagonal_zero}")

# 33. Verificar que a matriz é simétrica
# d(A, B) = d(B, A) porque cada diferença é elevada ao quadrado:
# (a - b)² = (b - a)². Logo a ordem dos registros não altera o resultado,
# e a matriz é igual à sua transposta.
simetrica = matriz.equals(matriz.T)
print(f"Matriz é simétrica? {simetrica}")
