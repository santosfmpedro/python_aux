import pandas as pd
import matplotlib.pyplot as plt
import os

def extrair_ano(data):
    return data.split('/')[-1]


def plot_ml(local):
    data = pd.read_csv(local)
    predicts = data[['PREDICT', 'CATEGORY','MODEL', 'DATE']]
    predicts = predicts.rename(columns={'PREDICT': 'VALUE'})

    real = data[['REAL', 'CATEGORY','MODEL', 'DATE']]
    real = real.drop_duplicates(subset=['REAL','CATEGORY', 'DATE'], keep='first')
    real['MODEL'] = 'REAL'
    real = real.rename(columns={'REAL': 'VALUE'})

    result = pd.concat([predicts, real], axis=0).reset_index().drop('index',axis = 1)

    # Aplicar a função 'extrair_ano' à coluna 'data' para criar uma nova coluna 'ano'
    result['year'] = result['DATE'].apply(extrair_ano)
    data = result

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
            plt.plot(model_data['year'], model_data['VALUE'], label=f'{model} - {category}', linestyle='-', marker='o')
            #plt.plot(model_data['DATE'], model_data['PREDICT'], label=f'{model} - Previsto', linestyle='--', marker='x')

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

import os

def plot_ml_save(local, output_folder):
    data = pd.read_csv(local)
    predicts = data[['PREDICT', 'CATEGORY','MODEL', 'DATE']]
    predicts = predicts.rename(columns={'PREDICT': 'VALUE'})

    real = data[['REAL', 'CATEGORY','MODEL', 'DATE']]
    real = real.drop_duplicates(subset=['REAL','CATEGORY', 'DATE'], keep='first')
    real['MODEL'] = 'REAL'
    real = real.rename(columns={'REAL': 'VALUE'})

    result = pd.concat([predicts, real], axis=0).reset_index().drop('index',axis = 1)

    # Aplicar a função 'extrair_ano' à coluna 'data' para criar uma nova coluna 'ano'
    result['year'] = result['DATE'].apply(extrair_ano)
    data = result

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
            plt.plot(model_data['year'], model_data['VALUE'], label=f'{model} - {category}', linestyle='-', marker='o')
        
        # Configurar o gráfico com legendas, títulos, rótulos dos eixos, etc.
        plt.xlabel('Data')
        plt.ylabel('Valor')
        plt.title(f'Gráfico para a Categoria: {category}')
        plt.legend()
        plt.grid(True)
        
        # Rotacionar as datas no eixo x para melhor visualização
        plt.xticks(rotation=45)
        
        # Salvar o gráfico em formato PNG na pasta de saída
        output_filename = os.path.join(output_folder, f'grafico_{category}.png')
        plt.savefig(output_filename)
        
        # Fechar o gráfico
        plt.close()
