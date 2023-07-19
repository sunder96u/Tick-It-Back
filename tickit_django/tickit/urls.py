from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter



urlpatterns = [

    path('venues/', views.VenueList.as_view(), name='venue_list'),
    path('venues/<int:pk>', views.VenueDetail.as_view(), name='venue-detail'),


    path('shows/', views.ShowList.as_view(), name='show_list'),
    path('shows/<int:pk>', views.ShowDetail.as_view(), name='show_detail'),


    path('bands/', views.BandList.as_view(), name='band_list'),
    path('bands/<int:pk>', views.BandDetail.as_view(), name='band_detail'),
]