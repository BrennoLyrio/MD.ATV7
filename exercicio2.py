# Exercício 2 — Qual cliente é mais semelhante ao cliente A?
# Atributos: [idade, compras por mês]
# Restrição: sem funções prontas de distância.

cliente_a = [25, 2]
cliente_b = [27, 3]
cliente_c = [45, 10]
cliente_d = [52, 12]

# 8. Distância entre A e B (cálculo manual)
dist_ab = ((cliente_a[0] - cliente_b[0]) ** 2 + (cliente_a[1] - cliente_b[1]) ** 2) ** 0.5

# 9. Distância entre A e C
dist_ac = ((cliente_a[0] - cliente_c[0]) ** 2 + (cliente_a[1] - cliente_c[1]) ** 2) ** 0.5

# 10. Distância entre A e D
dist_ad = ((cliente_a[0] - cliente_d[0]) ** 2 + (cliente_a[1] - cliente_d[1]) ** 2) ** 0.5

# 11 e 12. Comparar os resultados e encontrar a menor distância
distancias = {"B": dist_ab, "C": dist_ac, "D": dist_ad}

mais_proximo = None
menor_distancia = None
for cliente, dist in distancias.items():
    if menor_distancia is None or dist < menor_distancia:
        menor_distancia = dist
        mais_proximo = cliente

# 13. Exibir todas as distâncias e o cliente mais próximo
print("Distâncias em relação ao cliente A:")
for cliente, dist in distancias.items():
    print(f"  A -> {cliente}: {dist:.4f}")
print(f"\nCliente mais próximo de A: {mais_proximo} (distância {menor_distancia:.4f})")

# Por que a menor distância indica maior semelhança?
# A distância Euclidiana mede o quanto os valores dos atributos (idade e compras
# por mês) diferem entre dois clientes. Quanto menor a distância, menores são as
# diferenças entre esses atributos, ou seja, os clientes têm idade e comportamento
# de compra parecidos. Uma distância zero significaria clientes idênticos nesses
# atributos. Por isso, o cliente com a menor distância é o mais semelhante a A
# — considerando apenas os atributos utilizados.
