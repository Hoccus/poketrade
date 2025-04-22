import random
from collection.models import CollectionItem
from pokemonCard.models import PokemonCard

def give_random_pokemons_to_user(user, count=5):
    all_pokemon_ids = list(PokemonCard.objects.values_list('id', flat=True))

    selected_ids = random.sample(all_pokemon_ids, count)
    selected_pokemons = PokemonCard.objects.filter(id__in=selected_ids)

    for pokemon in selected_pokemons:
        CollectionItem.objects.create(
            user=user,
            pokemon=pokemon,
            status='collection'
        )