from django.db import models

# Create your models here.
class Images(models.Model):
    name = models.CharField(max_length = 60)
    description = models.TextField()
    image_location = models.ForeignKey('Location', on_delete=models.CASCADE,)
    image_category = models.ForeignKey('Category', on_delete=models.CASCADE,)
    
    @classmethod 
    def get_all_images(cls):
        images=cls.objects.all()
        return images
    
    @classmethod
    def save_image(self):
        self.save()
        
    @classmethod
    def delete_image(self):
        self.delete()
    
    
    
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
    
    @classmethod
    def save_location(self):
        self.save()
    
    @classmethod 
    def delete_location(self):
        self.delete()
        
        
    
    
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
    
    @classmethod
    def save_category(self):
        self.save()
        
    @classmethod
    def delete_category(self):
        self.delete()
    
    def __str__(self):
        return f"{self.cate}"