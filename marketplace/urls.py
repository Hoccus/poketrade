from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='marketplace.index'),
    path('<int:id>/', views.show, name='marketListings.show'),
]
