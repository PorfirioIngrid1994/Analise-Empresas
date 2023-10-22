import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Lendo a base de dados
Base_Dados = pd.read_excel('E:\\Empresas de Energia\\Dados_Empresas_Energia.xlsx')

# Verificando
Base_Dados.head()

# Serie Temporais - Setar o Index
Base_Dados.set_index('Data', inplace=True)

# VErificando
Base_Dados.head()

# Grafico

# Estilo do gráfico usando Seaborn
sns.set_style("darkgrid")

# Tamanho
plt.figure(figsize=(16, 7))

# Titulo
plt.title('Análise ações de empresas de Energia', loc='left', fontsize=18, fontweight=0)

# Plot da Petrobras
plt.plot(Base_Dados.index, Base_Dados['Petrobras'], color='#008c4a', linewidth=4, alpha=0.7)
# Texto da Petrobras
plt.text(Base_Dados.index[-1], Base_Dados['Petrobras'].tail(1), 'Petrobras', color='#008c4a', size='large', horizontalalignment='left')

# Plot de todas as colunas
for Coluna in Base_Dados.columns[1:]:
    # Plot das outras ações
    plt.plot(Base_Dados.index, Base_Dados[Coluna], color='gray', linewidth=2, alpha=0.7)
    # Texto das outras ações
    plt.text(Base_Dados.index[-1], Base_Dados[Coluna].tail(1), Coluna, color='gray', size='large', horizontalalignment='left')

# Labels
plt.xlabel('Período')
plt.ylabel('Preço de Fechamento (R$)')

# Exibindo o gráfico
plt.show()
