from django.shortcuts import render
from .models import Venue, Show, Band
from rest_framework import generics
from .serializers import BandSerializer, ShowSerializer, VenueSerializer

# Create your views here.



class VenueList(generics.ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class VenueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer




class BandList(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer

class BandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer





class ShowList(generics.ListCreateAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class ShowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer