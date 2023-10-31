"""Define URL patterns for khlep_site app."""

from django.urls import path

from . import views

app_name = 'khlep_site'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]