from django.urls import path

from . import views

urlpatterns = [
    path('', views.buy, name="buy"),
    path('login', views.login, name="login"),
    path('sell', views.sell, name="sell"),
    path('description', views.description, name="description"),
]