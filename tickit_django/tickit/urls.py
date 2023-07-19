from django.urls import path
from . import views



urlpatterns = [

    path('', views.venue_list, name='venue_list'),
    path('venues/<int:pk>', views.venue_detail, name='venue_detail'),


    path('shows/', views.show_list, name='show_list'),
    path('shows/<int:pk>', views.show_detail, name='show_detail'),


    path('bands/', views.band_list, name='band_list'),
    path('bands/<int:pk>', views.band_detail, name='band_detail'),
]