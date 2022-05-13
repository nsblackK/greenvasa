from django.urls import path

from . import views

urlpatterns = [
    # path('buy/', views.buy, name="buy"),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('buy/',views.buy, name='buy'),
    path('register/', views.register , name='register'),
    path('resetpwd/', views.resetpwd, name='resetpwd' ),
    path('changepwd/', views.changepwd, name='resetpwd'),
    path('sell/', views.sell, name="sell"),
    path('description/', views.description, name="description"),
]