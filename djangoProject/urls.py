"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from djangoProject.settings import STATIC_URL
from login import views as login_views
from django.contrib.auth import views as auth
from djangoProject import settings
from login import views as user_view


urlpatterns = [
    path('', include('login.urls')),
    path('sales', include('app1.urls')),
    path('admin/', admin.site.urls),
    path('login/',user_view.login, name='login'),
    path('logout',auth.LogoutView.as_view(template_name='landing_page.html'), name='logout'),
    path('register',user_view.register, name='register')

    
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)