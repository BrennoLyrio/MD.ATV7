# Exercício 1 — Distância Euclidiana entre dois clientes
# Atributos: [idade, compras por mês]
# Restrição: sem math.dist() ou qualquer função pronta de distância.

# 1. Armazenar os dados dos clientes em listas
cliente_a = [25, 2]
cliente_b = [28, 6]

# 2. Diferença entre as idades
dif_idade = cliente_a[0] - cliente_b[0]

# 3. Diferença entre as quantidades de compras
dif_compras = cliente_a[1] - cliente_b[1]

# 4. Elevar cada diferença ao quadrado
quad_idade = dif_idade ** 2
quad_compras = dif_compras ** 2

# 5. Somar os resultados
soma = quad_idade + quad_compras

# 6. Raiz quadrada da soma (expoente 0.5, sem usar função pronta de distância)
distancia = soma ** 0.5

# 7. Exibir a distância
print(f"Diferença de idade: {dif_idade} -> ao quadrado: {quad_idade}")
print(f"Diferença de compras: {dif_compras} -> ao quadrado: {quad_compras}")
print(f"Soma dos quadrados: {soma}")
print(f"Distância Euclidiana entre A e B: {distancia:.4f}")
