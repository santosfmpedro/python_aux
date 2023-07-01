import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV

def plot_ml_1(local):
    df = pd.read_csv('Data/data_plot_ml.csv')

    # Iterar sobre cada categoria
    categorias = df['CATEGORY'].unique()
    for categoria in categorias:
        # Filtrar os dados para a categoria atual
        dados_categoria = df[df['CATEGORY'] == categoria]

        # Configurar o gráfico
        plt.figure()

        # Iterar sobre cada modelo
        modelos = dados_categoria['MODEL'].unique()
        for modelo in modelos:
            # Filtrar os dados para o modelo atual
            dados_modelo = dados_categoria[dados_categoria['MODEL'] == modelo]

            # Plotar a linha com a coluna REAL
            plt.plot(dados_modelo['DATE'], dados_modelo['REAL'], label='REAL')

            # Plotar a linha com a coluna PREDICT
            plt.plot(dados_modelo['DATE'], dados_modelo['PREDICT'], label='PREDICT')

        # Adicionar legenda e título
        plt.legend()
        plt.title(f'Gráfico de Linhas - Categoria: {categoria}')

        # Exibir o gráfico
        plt.show()

def plot_ml_2(local):
    # Carregar os dados a partir do CSV
    data = pd.read_csv(local)

    # Obter todas as categorias únicas
    categories = data['CATEGORY'].unique()

    # Criar um gráfico para cada categoria
    for category in categories:
        # Filtrar os dados para a categoria atual
        category_data = data[data['CATEGORY'] == category]
        
        # Configurar o gráfico
        plt.figure(figsize=(10, 6))  # Definir tamanho da figura
        
        # Loop pelos modelos únicos para plotar linhas diferentes para cada modelo
        models = category_data['MODEL'].unique()
        for model in models:
            model_data = category_data[category_data['MODEL'] == model]
            
            # Plotar os valores reais e previstos para cada modelo
            plt.plot(model_data['DATE'], model_data['REAL'], label=f'{model} - Real', linestyle='-', marker='o')
            plt.plot(model_data['DATE'], model_data['PREDICT'], label=f'{model} - Previsto', linestyle='--', marker='x')

        # Configurar o gráfico com legendas, títulos, rótulos dos eixos, etc.
        plt.xlabel('Data')
        plt.ylabel('Valor')
        plt.title(f'Gráfico para a Categoria: {category}')
        plt.legend()
        plt.grid(True)
        
        # Rotacionar as datas no eixo x para melhor visualização
        plt.xticks(rotation=45)
        
        # Exibir o gráfico
        plt.tight_layout()  # Ajustar layout para evitar corte de elementos
        plt.show()
