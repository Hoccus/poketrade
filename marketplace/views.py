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
    return render(request, 'marketplace/show.html',
    {'template_data': template_data})
# Create your views here.
