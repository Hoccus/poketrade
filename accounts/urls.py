from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', views.signup, name='accounts.signup'),
    path('login', views.login, name='accounts.login'),
    path('logout', views.logout, name='accounts.logout'),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="accounts/reset_password.html"), name="reset_password"),
]