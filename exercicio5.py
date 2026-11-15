# Exercício 5 — Influência da escala e normalização
import math

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 22. Criar o DataFrame
df = pd.DataFrame(
    {
        "Idade": [20, 25, 40, 55, 70],
        "Renda": [2000, 3000, 6000, 9000, 12000],
    },
    index=["A", "B", "C", "D", "E"],
)
df.index.name = "Cliente"

print("Dados originais:")
print(df)

# 23. Distância entre A e B com os valores originais
dist_original = math.dist(df.loc["A"], df.loc["B"])
print(f"\nDistância A -> B (valores originais): {dist_original:.4f}")

# 24. Normalizar Idade e Renda com MinMaxScaler (escala 0 a 1)
scaler = MinMaxScaler()
df_norm = pd.DataFrame(
    scaler.fit_transform(df[["Idade", "Renda"]]),
    columns=["Idade", "Renda"],
    index=df.index,
)

# 25. Exibir o DataFrame normalizado
print("\nDados normalizados (MinMaxScaler):")
print(df_norm.round(4))

# 26. Distância entre A e B com os valores normalizados
dist_norm = math.dist(df_norm.loc["A"], df_norm.loc["B"])
print(f"\nDistância A -> B (valores normalizados): {dist_norm:.4f}")

# 27. Comparação dos resultados
print("\nComparação:")
print(f"  Original:    {dist_original:.4f}")
print(f"  Normalizada: {dist_norm:.4f}")
print(
    f"  Nos dados originais, a diferença de renda (1000) contribui com "
    f"{1000**2} para a soma dos quadrados, enquanto a de idade (5) contribui só com {5**2}."
)

# Por que a renda tem influência muito maior com os valores originais?
# A distância Euclidiana soma os quadrados das diferenças de cada atributo sem
# considerar a unidade ou a escala. A renda varia na casa dos milhares
# (2.000 a 12.000), enquanto a idade varia na casa das dezenas (20 a 70). Assim,
# uma diferença de R$ 1.000 pesa muito mais do que uma diferença de 5 anos, e a
# distância passa a refletir quase só a renda — a idade praticamente é ignorada.
# Com a normalização Min-Max, os dois atributos passam para o intervalo [0, 1]
# e contribuem de forma equilibrada para a distância.
