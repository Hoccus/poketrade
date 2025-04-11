import requests
from django.shortcuts import render


def get_cards(request):
    url = "https://pokeapi.co/api/v2/pokemon?limit=20"  # Get first 20 Pokémon
    response = requests.get(url)

    if response.status_code == 200:
        raw_data = response.json()["results"]

        # Get name + sprite from individual Pokémon detail endpoint
        pokemon_list = []
        for entry in raw_data:
            poke_resp = requests.get(entry["url"])
            if poke_resp.status_code == 200:
                poke_data = poke_resp.json()
                pokemon_list.append({
                    "name": poke_data["name"].capitalize(),
                    "sprite": poke_data["sprites"]["front_default"]  # front_default = normal small sprite
                })
    else:
        pokemon_list = []

    return render(request, 'collection/index.html', {'pokemon_list': pokemon_list})