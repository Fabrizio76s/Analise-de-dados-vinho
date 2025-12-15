# Analise de dados vinho
```markdown
#  Análise Estatística de Qualidade de Vinhos Tintos

Este projeto realiza uma análise exploratória de dados (EDA) e testes de hipótese para investigar os fatores físico-químicos que influenciam a qualidade do vinho tinto.

O código utiliza visualizações interativas e testes estatísticos rigorosos (Teste T de Student) para validar quais componentes (como álcool e sulfatos) diferenciam vinhos de alta qualidade dos demais.

##  Bibliotecas Utilizadas

O projeto foi desenvolvido em Python utilizando as seguintes bibliotecas:

* **Pandas:** Manipulação do dataset e cálculos descritivos.
* **Plotly (Graph Objects & Subplots):** Criação de histogramas e boxplots interativos.
* **Seaborn:** Visualização de correlações complexas (`pairplot`).
* **SciPy (Stats):** Execução de testes de hipótese (Teste T).
* **Google Colab:** Ferramentas de upload de arquivos na nuvem.

##  Estrutura da Análise

O script segue o seguinte fluxo lógico:

1.  **Carregamento de Dados:** Upload manual do arquivo `winequality-red.csv` via widget do Google Colab.
2.  **Estatística Descritiva:** Análise inicial dos tipos de dados (`dtypes`) e resumo estatístico (`describe`).
3.  **Visualização Interativa (Plotly):**
    * **Histogramas:** Para analisar a distribuição de frequência de todas as 12 variáveis.
    * **Boxplots:** Para identificação visual de *outliers* e dispersão dos dados.
4.  **Correlação:** Análise da correlação linear das variáveis com a coluna alvo `quality`.
5.  **Teste de Hipóteses (Inferência):**
    * Comparação entre grupos de **Vinhos Ruins** (notas $\le$ 4) e **Vinhos Bons** (notas $\ge$ 7).
    * Aplicação do **Teste T** para validar a significância do **Teor Alcoólico** e dos **Sulfatos**.

##  Resultados dos Testes de Hipótese

O código foca em responder se as diferenças observadas visualmente são estatisticamente reais.

### 1. Teor Alcoólico
O teste compara se vinhos "Bons" possuem mais álcool que vinhos "Ruins".
* **Resultado esperado:** P-valor < 0.05.
* **Conclusão:** Rejeita-se a hipótese nula. A diferença no teor alcoólico é estatisticamente significativa e não fruto do acaso.

### 2. Sulfatos
O teste verifica a influência dos sulfatos (conservantes/antioxidantes) na qualidade.
* **Resultado esperado:** P-valor < 0.05.
* **Conclusão:** Há evidência estatística de que vinhos melhores possuem concentrações diferentes (geralmente maiores) de sulfatos.

##  Como Executar

1.  Tenha o arquivo `winequality-red.csv` em sua máquina (disponível no [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/wine+quality)).
2.  Abra o notebook no Google Colab.
3.  Execute a célula de upload:
    ```python
    from google.colab import files
    files.upload()
    ```
4.  Certifique-se de que o caminho do arquivo no `pd.read_csv` corresponde ao local onde o arquivo foi salvo (ex: `/content/winequality-red.csv`).

---
*Projeto desenvolvido para fins de estudo em Ciência de Dados e Estatística Computacional.*

```