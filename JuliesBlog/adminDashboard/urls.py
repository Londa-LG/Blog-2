"""
URL configuration for JuliesBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from adminDashboard import views

app_name = "Dashboard"

urlpatterns = [
	path("login/", views.Login, name="admin-login"),
	path("logout/", views.Logout, name="admin-logout"),
	path("", views.Dashboard, name="admin-dashboard"),
	path("posts/", views.Posts, name="admin-posts"),
	path("editpost/<slug:post>/", views.Edit_Post, name="admin-edit-post"),
	path("createpost/", views.Create_Post, name="admin-create-post"),
]
