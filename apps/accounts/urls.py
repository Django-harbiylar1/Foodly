from django.urls import path

from apps.accounts.views import login

urlpatterns = [
    path('login/', login, name='login'),
]