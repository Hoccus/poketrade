from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from collection.models import CollectionItem
from marketplace.models import MarketListing


@login_required
def create_listing(request, id):
    if request.method == 'POST' and request.POST['price'] != '':
        item = get_object_or_404(CollectionItem, id=id, user=request.user)
        item.status = 'listed'
        item.save()
        marketListing = MarketListing()
        marketListing.price = request.POST['price']
        marketListing.item = item
        marketListing.seller = request.user
        marketListing.save()
        return redirect('collection.detail', id=id)
    else:
        return redirect('collection.detail', id=id)

@login_required
def delete_listing(request, id, listing_id):
    item = get_object_or_404(CollectionItem, id=id, user=request.user)
    item.status = 'collection'
    item.save()
    listing = get_object_or_404(MarketListing, id=listing_id)
    listing.delete()
    return redirect('collection.detail', id=id)
@login_required
def user_collection(request):
    cards = CollectionItem.objects.filter(user=request.user).select_related('pokemon')
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
    if item.status == 'listed':
        marketListing = MarketListing.objects.get(item=item)
    item.hp_percent = round(pokemon.hp / 255 * 100, 2)
    item.attack_percent = round(pokemon.attack / 190 * 100, 2)
    item.defense_percent = round(pokemon.defense / 230 * 100, 2)
    if item.status == 'listed':
        marketListing = MarketListing.objects.get(item=item)
    else:
        marketListing = None
    return render(request, 'collection/detail.html', {'item': item, 'marketListing': marketListing})