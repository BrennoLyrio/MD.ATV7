# Exercício 4 — Comparando vários clientes com math.dist()
# Atributos: [idade, compras por mês]

# 18. Importar o módulo math
import math

clientes = {
    "A": [25, 2],
    "B": [27, 3],
    "C": [30, 5],
    "D": [45, 10],
    "E": [52, 12],
}

referencia = clientes["A"]

# 19 e 20. Calcular e exibir a distância de A para os demais clientes
distancias = {}
print("Distâncias em relação ao cliente A:")
for nome, atributos in clientes.items():
    if nome == "A":
        continue
    distancias[nome] = math.dist(referencia, atributos)
    print(f"  A -> {nome}: {distancias[nome]:.4f}")

# 21. Identificar automaticamente o cliente mais próximo
mais_proximo = min(distancias, key=distancias.get)

print(
    f"\nO cliente {mais_proximo} possui o perfil mais próximo de A, "
    f"considerando idade e compras por mês (distância {distancias[mais_proximo]:.4f})."
)
