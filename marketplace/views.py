from django.shortcuts import render
from .models import MarketListing
def index(request):
    template_data = {}
    template_data['title'] = 'Listings'
    template_data['listings'] = MarketListing.objects.all()
    return render(request, 'marketplace/index.html',
    {'template_data': template_data})

# Create your views here.
