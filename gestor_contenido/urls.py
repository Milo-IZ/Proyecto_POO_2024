"""
URL configuration for gestor_contenido project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from investigaciones import views
from django.contrib.auth.views import LogoutView
from investigaciones.views import logout_view
from investigaciones.views import mis_investigaciones

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('foro/', views.foro, name='foro'),
    path('post/<int:id>/', views.post, name='post'),
    path('form_post/', views.crear_contenido, name='form_post'),
    path('denuncia/', views.denunciar, name='denuncia'),
    path('voto/', views.voto, name='voto'), 
    path('profile/', views.profile, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('mis-investigaciones/', mis_investigaciones, name='mis_investigaciones'),
]
