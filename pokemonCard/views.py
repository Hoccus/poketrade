from django.shortcuts import render

# Create your views here.
import requests
from .models import PokemonCard
def fetch_and_store_pokemon():
    base_url = "https://pokeapi.co/api/v2/pokemon?limit=1000"
    response = requests.get(base_url)

    if response.status_code == 200:
        for pokemon in response.json()['results']:
            detail = requests.get(pokemon['url'])
            if detail.status_code == 200:
                data = detail.json()
                name = data['name'].capitalize()
                sprite = data['sprites']['front_default']
                hp = next((stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'hp'), None)
                attack = next((stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'attack'), None)

                PokemonCard.objects.get_or_create(
                    name=name,
                    defaults={
                        'image_url': sprite,
                        'hp': hp,
                        'attack': attack,
                        'description': 'no description',
                    }
                )