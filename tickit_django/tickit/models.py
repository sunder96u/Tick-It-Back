from django.db import models

class Venue(models.Model):
    venue_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    capacity = models.IntegerField(default=0)
    type = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    venue_photo = models.ImageField(default="No photo available")

    def __str__(self):
        return self.name
    

        
class Band(models.Model):
    band_id = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=100, default="")
    genre = models.CharField(max_length=100, default="")
    logo = models.ImageField(default="No Logo Provided")

    def __str__(self):
        return self.name

    

class Show(models.Model):
    show_id = models.CharField(max_length=100, default="")
    venue_id = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='venue', default="")
    title = models.CharField(max_length=100, default="No Title Available")
    time = models.CharField(max_length=100, default="12:00pm")
    starting_price = models.CharField(max_length=100, default="1")
    poster = models.ImageField(default="No Poster Provided")
    band_id = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='band', default="")

    def __str__(self):
        return self.title
    
