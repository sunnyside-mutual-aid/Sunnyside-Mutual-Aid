from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_help/', views.get_help, name='get_help'),
    path('volunteer/', views.volunteer, name='volunteer'),
]
