from django.urls import path
from . import views
urlpatterns = [
    path('', views.user_collection, name='collection.get_cards'),
    path('<int:id>/', views.pokemon_detail, name='collection.detail'),
    path('toggle_favorite/<int:id>/', views.toggle_favorite, name='collection.toggle_favorite'),
]