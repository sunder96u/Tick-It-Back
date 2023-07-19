from rest_framework import serializers
from .models import Venue, Show, Band

class VenueSerializer(serializers.HyperlinkedModelSerializer):
    shows = serializers.HyperlinkedRelatedField(
        view_name = 'show_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Venue
        fields = ('id', 'venue_id','name','address','capacity','type','contact','venue_photo')




class ShowSerializer(serializers.HyperlinkedModelSerializer):
    bands = serializers.HyperlinkedRelatedField(
        view_name = 'band_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Show
        fields = ('show_id','venue_id','title','time','starting_price','poster')



class BandSerializer(serializers.HyperlinkedModelSerializer):
    shows = serializers.HyperlinkedRelatedField(
        view_name = 'show_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Band
        fields =(all)