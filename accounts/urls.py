from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', views.signup, name='accounts.signup'),
    path('login', views.login, name='accounts.login'),
    path('logout', views.logout, name='accounts.logout'),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="accounts/reset_password.html"), name="reset_password"),
    path('orders/', views.orders, name='accounts.orders'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="accounts/reset_password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/reset_password_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/reset_password_complete.html"), name="password_reset_complete"),
    path('add-pokecoin/', views.add_pokecoin, name='add-pokecoin'),
    path('get-random-pokemon/', views.get_random_pokemon, name='get-random-pokemon'),
]