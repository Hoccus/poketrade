from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from marketplace.models import MarketListing
from .utils import calculate_cart_total
from .models import Order, CartItem
from django.contrib.auth.decorators import login_required

@login_required
def purchase(request):
    cart = request.session.get('cart', {})
    listing_ids = list(cart.keys())
    if (listing_ids == []):
        return redirect('cart.index')
    listings_in_cart = MarketListing.objects.filter(id__in=listing_ids)
    cart_total = calculate_cart_total(cart, listings_in_cart)
    order = Order()
    order.user = request.user
    order.total = cart_total
    order.save()
    for listing in listings_in_cart:
        item = CartItem()
        item.marketListing = listing
        item.price = listing.price
        item.order = order
        item.save()
    request.session['cart'] = {}
    template_data = {}
    template_data['title'] = 'Purchase confirmation'
    template_data['order_id'] = order.id
    return render(request, 'cart/purchase.html',{'template_data': template_data})

def index(request):
    cart_total = 0
    listings_in_cart = []
    cart = request.session.get('cart', {})
    listing_ids = list(cart.keys())
    if (listing_ids != []):
        listings_in_cart = MarketListing.objects.filter(id__in=listing_ids)
        cart_total = calculate_cart_total(cart, listings_in_cart)
    template_data = {}
    template_data['title'] = 'Cart'
    template_data['listings_in_cart'] = listings_in_cart
    template_data['cart_total'] = cart_total
    return render(request, 'cart/index.html',
    {'template_data': template_data})

def add(request, id):
    listing = get_object_or_404(MarketListing, id=id)
    cart = request.session.get('cart', {})
    cart[id] = 1
    request.session['cart'] = cart
    listing.inCart = True
    listing.save()
    return redirect('cart.index')
def clear(request):
    cart = request.session.get('cart', {})
    listing_ids = list(cart.keys())
    listings_in_cart = MarketListing.objects.filter(id__in=listing_ids)
    for listing in listings_in_cart:
        listing.inCart = False
        listing.save()
    request.session['cart'] = {}
    return redirect('cart.index')

# Create your views here.
