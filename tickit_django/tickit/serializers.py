from rest_framework import serializers
from .models import Venue, Show, Band



class BandSerializer(serializers.HyperlinkedModelSerializer):
    shows = serializers.HyperlinkedRelatedField(
        view_name = 'show-detail',
        many=True,
        read_only=True
    )


    venue_id = serializers.PrimaryKeyRelatedField(
        queryset= Venue.objects.all(),
        source='venue'
    )

    class Meta:
        model = Band
        fields ='__all__'



class VenueSerializer(serializers.HyperlinkedModelSerializer):
    shows = BandSerializer(
        many=True,
        read_only=True
    )

    venue_url = serializers.ModelSerializer.serializer_url_field(
        view_name='venue-detail'
    )


    class Meta:
        model = Venue
        fields = '__all__'




class ShowSerializer(serializers.HyperlinkedModelSerializer):
    bands = BandSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Show
        fields ='__all__'



