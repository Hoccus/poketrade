from django.urls import path
from . import views
urlpatterns = [
    path('<int:id>/marketListing/<int:listing_id>/delete/', views.delete_listing, name='collection.delete_listing'),
    path('<int:id>/marketListing/create/', views.create_listing, name='collection.create_listing'),
    path('', views.user_collection, name='collection.get_cards'),
    path('<int:id>/', views.pokemon_detail, name='collection.detail'),
    path('toggle_favorite/<int:id>/', views.toggle_favorite, name='collection.toggle_favorite'),
]