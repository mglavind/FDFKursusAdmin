"""
SKSBooking2023 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    #path('', include('organization.urls')),
    path('', login_required(views.index), name='index'),  # Protect the view with login_required
    path('admin/', admin.site.urls),
    path('organization/', include('django.contrib.auth.urls')),
    path('organization/', include('organization.urls')),
    path('Foto/', include('Foto.urls')),
    path('Teknik/', include('Teknik.urls')),
    path('Butikken/', include('Butikken.urls')),
    path('AktivitetsTeam/', include('AktivitetsTeam.urls')),
    path('Location/', include('Location.urls')),
    path('Sjak/', include('Sjak.urls')),
    path('Depot/', include('Depot.urls')),
    path('SOS/', include('SOS.urls')),
    path('Support/', include('Support.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('submit-todo', views.submit_todo, name='submit-todo'),
    path('complete-todo/<int:pk>/', views.complete_todo, name='complete-todo'),
    path('delete-todo/<int:pk>/', views.delete_todo, name='delete-todo'),
    path(r'comments/', include('django_comments_xtd.urls')),

]

# Configure Admin Titles
admin.site.site_header = "Sletten admin"
admin.site.site_title = "Sletten admin"
admin.site.index_title = "Velkommen teamleder!"

