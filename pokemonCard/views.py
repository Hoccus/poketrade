# Create your views here.
import requests
from .models import PokemonCard
def get_english_description(species_data):
    for entry in species_data['flavor_text_entries']:
        if entry['language']['name'] == 'en':
            return entry['flavor_text'].replace('\n', ' ').replace('\f', ' ')
    return "No description available."

def fetch_and_store_pokemon(limit):
    base_url = "https://pokeapi.co/api/v2/pokemon?limit=" + str(limit)
    response = requests.get(base_url)

    if response.status_code == 200:
        for pokemon in response.json()['results']:
            detail = requests.get(pokemon['url'])
            if detail.status_code == 200:
                data = detail.json()
                name = data['name'].capitalize()
                type = [t['type']['name'] for t in data['types']]
                type_str = ", ".join(type)
                sprite = data['sprites']['front_default']
                hp = next((stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'hp'), None)
                attack = next((stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'attack'), None)
                defense = next((stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'defense'), None)

                species_url = data['species']['url']
                species_resp = requests.get(species_url)
                if species_resp.status_code == 200:
                    species_data = species_resp.json()
                    description = get_english_description(species_data)
                else:
                    description = "No description available."
                PokemonCard.objects.update_or_create(
                    name=name,
                    defaults={
                        'image_url': sprite,
                        'type': type_str,
                        'hp': hp,
                        'attack': attack,
                        'defense': defense,
                        'description': description,
                    }
                )