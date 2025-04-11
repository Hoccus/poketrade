from django.urls import path
from . import views
urlpatterns = [
    path('', views.get_cards, name='collection.get_cards'),
]