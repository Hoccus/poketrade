from django.shortcuts import render

def index(request):
    template_data = {'title': 'PokéTrade'}
    return render(request, 'index.html', {'template_data': template_data})
def about(request):
    return render(request, 'about.html')