import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carregar os dados
df = pd.read_csv('dadosVendas.csv')

# 2. Gráfico de Barras: Desempenho dos Vendedores
plt.figure(figsize=(10, 6))
vendas_vendedor = df.groupby('Vendedor')['Valor_Total'].sum().reset_index().sort_values('Valor_Total', ascending=False)
sns.barplot(data=vendas_vendedor, x='Vendedor', y='Valor_Total', palette='viridis')
plt.title('Total de Vendas por Vendedor')
plt.show()

# 3. Gráfico de Dispersão: Relação Preço x Quantidade
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Quantidade', y='Valor_Unitario', hue='Produto', size='Valor_Unitario', sizes=(20, 200), alpha=0.7)
plt.title('Correlação: Valor vs Quantidade por Produto')
plt.show()

# 4. Mapa de Calor: Onde os produtos mais vendem?
plt.figure(figsize=(10, 6))
heatmap_data = df.pivot_table(index='Regiao', columns='Produto', values='Valor_Unitario', aggfunc='sum')
sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap='YlGnBu')
plt.title('Vendas por Região e Produto')
plt.show()