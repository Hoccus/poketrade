from django.urls import path
from . import views

urlpatterns = [
    path('', views.trade_list, name='trade.list'),
    path('initiate/<int:user_id>/', views.initiate_trade, name='trade.initiate'),
    path('create/', views.create_trade, name='trade.create'),
    path('accept/<int:trade_id>/', views.accept_trade, name='trade.accept'),
    path('reject/<int:trade_id>/', views.reject_trade, name='trade.reject'),

    path('users/', views.users_list, name='trade.users_list'),
]