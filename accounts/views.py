from idlelib.rpc import request_queue
from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import CustomUserCreationForm, CustomErrorList
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from collection.utils import give_random_pokemons_to_user
from django.contrib.auth.models import User
@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')

def login(request):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(
            request, username = request.POST['username'], password = request.POST['password']
        )
        if user is None:
            template_data['error'] = 'The username or password you entered is invalid.'
            return render(request, 'accounts/login.html', {'template_data': template_data})
        else:
            auth_login(request, user)
            return redirect('home.index')

def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {'template_data': template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            user = form.save()
            give_random_pokemons_to_user(user)
            return redirect('accounts.login')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html', {'template_data': template_data})

@login_required
def orders(request):
    template_data = {}
    template_data['title'] = 'Orders'
    template_data['orders'] = request.user.orders.all()
    return render(request, 'accounts/orders.html', {'template_data': template_data})

@login_required
def add_pokecoin(request):
    if request.method == 'POST':
        profile = request.user.userprofile
        profile.pokeCoins += 1
        profile.save()
        return redirect('add-pokecoin')

    return render(request, 'accounts/add_pokecoin.html')

@login_required
def get_random_pokemon(request):
    if request.method == 'POST':
        if request.user.userprofile.pokeCoins < 50:
            return redirect('/accounts/add-pokecoin/?error=not_enough_coins')
        request.user.userprofile.pokeCoins -= 50
        request.user.userprofile.save()
        give_random_pokemons_to_user(request.user, count=1)
    return redirect('collection.get_cards')