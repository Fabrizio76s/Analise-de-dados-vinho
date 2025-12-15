from google.colab import files
files.upload()

import pandas as pd
from scipy import stats
df=pd.read_csv('/content/dados/winequality-red.csv',sep=';')
df


df.dtypes
df.describe()
len(df.columns)

from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=6, cols=2, subplot_titles=(
    df.columns
))
j=1
k=0
for i in list(df.columns):
    k=k+1
    fig.add_trace(
        go.Histogram(
            x=df[i], name=i
        ), row=j, col=k
    )
    j=j+1 if k==2 else j
    k=0 if k==2 else k
fig.update_layout(
    title_text="Histogramas",
    showlegend=True,
    height=2000,
    width=750
)

from plotly.subplots import make_subplots
import plotly.graph_objects as go
fig = make_subplots(rows=6, cols=2, subplot_titles=(
    df.columns
))
j=1
k=0
for i in list(df.columns):
    k=k+1
    fig.add_trace(
        go.Box(
            x=df[i], name=i
        ), row=j, col=k
    )
    j=j+1 if k==2 else j
    k=0 if k==2 else k
fig.update_layout(
    title_text="Histogramas",
    showlegend=True,
    height=2000,
    width=750
)

df.corr()['quality']

sns.pairplot(df,hue='quality')



vinhos_ruins = df[df['quality'] <= 4]['alcohol']  # Qualidade Baixa
vinhos_bons = df[df['quality'] >= 7]['alcohol']   # Qualidade Alta
stat, p_valor = stats.ttest_ind(vinhos_bons, vinhos_ruins)


print(f"Estatística T: {stat}")
print(f"P-valor: {p_valor}")
if p_valor < 0.05:
    print("Resultado: Rejeitamos a hipótese nula.")
    print("Conclusão: A diferença no teor alcoólico é estatisticamente significativa. Não foi sorte.")
else:
    print("Resultado: Não podemos rejeitar a hipótese nula.")
    print("Conclusão: A diferença observada pode ser apenas acaso.")
    import pandas as pd
from scipy import stats


sulfatos_ruins = df[df['quality'] <= 4]['sulphates']  # Qualidade Baixa
sulfatos_bons = df[df['quality'] >= 7]['sulphates']   # Qualidade Alta


stat, p_valor = stats.ttest_ind(sulfatos_bons, sulfatos_ruins)

print(f"Estatística T (Sulfatos): {stat}")
print(f"P-valor: {p_valor}")


print("-" * 30)
if p_valor < 0.05:
    print("Resultado: Rejeitamos a hipótese nula.")
    print("Conclusão: A quantidade de sulfatos é significativamente diferente em vinhos bons vs. ruins.")
    
    if stat > 0:
        print("Obs: Os vinhos BONS têm, em média, mais sulfatos.")
    else:
        print("Obs: Os vinhos RUINS têm, em média, mais sulfatos.")
else:
    print("Resultado: Não podemos rejeitar a hipótese nula.")
    print("Conclusão: A diferença nos sulfatos não é estatisticamente relevante (pode ser acaso).")
