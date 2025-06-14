"""Members URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('add/', login_required(views.add_member), name='add_member'),
    path('search/', login_required(views.search_member), name='search_member'),
    path('view/', login_required(views.view_member), name='view_member'),
    path('delete/<int:id>/', login_required(views.delete_member), name='delete_member'),
    path('update/<int:id>/', login_required(views.update_member), name='update_member'),
    path('', login_required(views.members), name='members'),
]
