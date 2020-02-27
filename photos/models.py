from django.db import models

# Create your models here.
class Images(models.Model):
    name = models.CharField(max_length = 60)
    description = models.TextField()
    image_location = models.ForeignKey('Location', on_delete=models.CASCADE,)
    image_category = models.ForeignKey('Category', on_delete=models.CASCADE,)
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    locations=(
        ('Zuri','Zuri'),
        ('China','China'),
        ('Wuhan','Wuhan'),
        ('Turkey','Turkey'),
        ('Mexico','Mexico'),
        ('Paris','Paris'),
    )
    locs = models.CharField(max_length = 255, choices = locations)
    
    def __str__(self):
        return f"{self.locs}"


    
class Category(models.Model):
    categories = (
        ('Flowers','Flowers'),
        ('Articles','Articles'),
        ('Animals','Animals'),
        ('People','People')
    )
    cate = models.CharField(max_length = 255, choices = categories)
    
    def __str__(self):
        return f"{self.cate}"