from django.urls import path
from . import views
urlpatterns = [
    path('', views.user_collection, name='collection.get_cards'),

]