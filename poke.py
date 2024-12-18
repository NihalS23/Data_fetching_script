import requests
import csv

def fetch_pokemon_data(pokemon_id):
    api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return {
            "name": data.get("name"),
            "height": data.get("height"),
            "weight": data.get("weight")
        }
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred for Pokémon ID {pokemon_id}: {http_err}")
    except Exception as err:
        print(f"Other error occurred for Pokémon ID {pokemon_id}: {err}")
    return None

def save_to_csv(data, filename, columns):
    if not data:
        print("No data to save.")
        return

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=columns)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"I/O error occurred: {e}")

if __name__ == "__main__":
    # Fetch data for the first 50 Pokémon
    columns = ['name', 'height', 'weight','base_experience']
    pokemon_data = []
    
    for pokemon_id in range(1, 51):  # Pokémon IDs from 1 to 50
        data = fetch_pokemon_data(pokemon_id)
        if data:
            pokemon_data.append(data)
    
    if pokemon_data:
        save_to_csv(pokemon_data, "pokemon_data.csv", columns)
    else:
        print("Failed to fetch data.")
