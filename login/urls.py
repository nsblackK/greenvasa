from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('buy/',views.buy, name='buy'),
    path('register/', views.register , name='register'),
    path('resetpwd/', views.resetpwd, name='resetpwd' ),
    path('changepwd/', views.changepwd, name='resetpwd'),
    path('sell/', views.sell, name="sell"),
    path('description/', views.description, name="description"),
]