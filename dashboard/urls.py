from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.index, name = 'dashboard-index'),
    path('dashboard/guest/', views.guest_home, name = 'guest-index'),
]