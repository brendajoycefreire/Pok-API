import requests
import pandas as pd

url = "https://pokeapi.co/api/v2/pokemon?limit=100"  # Limitando para pegar 100 Pokémon
response = requests.get(url)
data = response.json()

# Lista para armazenar os dados dos Pokémon
pokemon_data = []

# Para cada Pokémon listado, fazemos uma requisição para obter os detalhes completos
for pokemon in data['results']:
    pokemon_url = pokemon['url']
    pokemon_details = requests.get(pokemon_url).json()
    
    # Coletando os dados desejados
    pokemon_data.append({
        'name': pokemon['name'],
        'id': pokemon_details['id'],
        'height': pokemon_details['height'],
        'weight': pokemon_details['weight'],
        'abilities': [ability['ability']['name'] for ability in pokemon_details['abilities']]  # Coletando todas as habilidades
    })

# Criar um DataFrame do pandas
df_bronze = pd.DataFrame(pokemon_data)

# Salvar os dados em um arquivo CSV
df_bronze.to_csv('pokemon_bronze.csv', index=False)

# Exibir as primeiras linhas do DataFrame
print(df_bronze.head())

