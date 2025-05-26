# Requests = connect to an API

import requests

base_url = "https://pokeapi.co/api/v2/"


def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None


def main():
    pokemon_name = "charizard"
    pokemon_info = get_pokemon_info(name=pokemon_name)

    if pokemon_info:
        print(f"ID: {pokemon_info['id']}")
        print(f"Name: {pokemon_info['name'].capitalize()}")
        print(f"Height: {pokemon_info['height']}")
        print(f"Weight: {pokemon_info['weight']}")

        types = pokemon_info['types']
        types = [type['type'].get('name') for type in types]

        print(f"Types: {types}")


if __name__ == "__main__":
    main()
