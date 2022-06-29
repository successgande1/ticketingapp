from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'pages-index'),
    path('about/', views.about, name = 'pages-about'),
    
]