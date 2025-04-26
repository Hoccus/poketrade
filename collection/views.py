from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from collection.models import CollectionItem

@login_required
def user_collection(request):
    cards = CollectionItem.objects.filter(user=request.user, status='collection').select_related('pokemon')
    return render(request, 'collection/index.html', {
        'user_pokemon_list': cards
    })

@login_required
def toggle_favorite(request, id):
    item = get_object_or_404(CollectionItem, id=id, user=request.user)
    if item.status == 'collection':
        item.status = 'pending'
    elif item.status == 'pending':
        item.status = 'collection'
    item.save()
    return redirect('collection.detail', id=id)
@login_required
def pokemon_detail(request, id):
    item = get_object_or_404(CollectionItem, id=id, user=request.user)
    pokemon = item.pokemon

    item.hp_percent = round(pokemon.hp / 255 * 100, 2)
    item.attack_percent = round(pokemon.attack / 190 * 100, 2)
    item.defense_percent = round(pokemon.defense / 230 * 100, 2)

    return render(request, 'collection/detail.html', {'item': item})