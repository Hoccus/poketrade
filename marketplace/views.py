from django.shortcuts import render
from .models import MarketListing
def index(request):
    template_data = {}
    template_data['title'] = 'Listings'
    template_data['listings'] = MarketListing.objects.filter(inCart=False)
    return render(request, 'marketplace/index.html',
    {'template_data': template_data})
def show(request, id):
    marketListing = MarketListing.objects.get(id=id)
    template_data = {}
    template_data['title'] = marketListing.item.pokemon.name
    template_data['listing'] = marketListing
    pokemon = marketListing.item.pokemon
    template_data['hp_percent'] = round(pokemon.hp / 255 * 100, 2)
    template_data['attack_percent'] = round(pokemon.attack / 190 * 100, 2)
    template_data['defense_percent'] = round(pokemon.defense / 230 * 100, 2)
    return render(request, 'marketplace/show.html',
    {'template_data': template_data})
# Create your views here.
