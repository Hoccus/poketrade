from django.shortcuts import render

def index(request):
    template_data = {'title': 'Movies Store'}
    return render(request, 'index.html', {'template_data': template_data})
def about(request):
    return render(request, 'about.html')