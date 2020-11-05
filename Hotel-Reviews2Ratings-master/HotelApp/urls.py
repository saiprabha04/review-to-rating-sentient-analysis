from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('search/', views.search,name='search'),
    path('hotels/', views.hotels,name='hotels'),
    path('searched/', views.searched,name='searched'),
    path('review/<int:id>', views.review,name='review'),
]
