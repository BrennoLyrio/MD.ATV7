# Exercício 3 — Distância Euclidiana com três atributos
# Atributos: [nota média, frequência (%), horas de estudo por semana]
# Restrição: sem funções prontas de distância.

aluno_a = [8.0, 92, 10]
aluno_b = [7.8, 90, 9]
aluno_c = [5.2, 68, 3]


def distancia_euclidiana(p, q):
    """Calcula manualmente a distância Euclidiana entre dois vetores
    de mesmo tamanho: raiz da soma dos quadrados das diferenças."""
    soma = 0
    for i in range(len(p)):
        soma += (p[i] - q[i]) ** 2
    return soma ** 0.5


# 14. Distância entre A e B
dist_ab = distancia_euclidiana(aluno_a, aluno_b)

# 15. Distância entre A e C
dist_ac = distancia_euclidiana(aluno_a, aluno_c)

# 16. Exibir os resultados
print(f"Distância A -> B: {dist_ab:.4f}")
print(f"Distância A -> C: {dist_ac:.4f}")

# 17. Aluno mais próximo de A
if dist_ab < dist_ac:
    print("O aluno B está mais próximo de A.")
elif dist_ac < dist_ab:
    print("O aluno C está mais próximo de A.")
else:
    print("B e C estão à mesma distância de A.")

# Observação: a lógica é a mesma usada em duas dimensões. Para cada atributo
# calcula-se a diferença, eleva-se ao quadrado, somam-se todos os quadrados e
# extrai-se a raiz. Com três atributos, basta incluir mais um termo na soma —
# a fórmula vale para qualquer número de dimensões.
