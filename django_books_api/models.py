from django.db import models

# Create your models here
class Book(models.Model):
    title = models.CharField(max_length=150)
    Author = models.CharField(max_length=150, default='yusuf')
    category = models.CharField(max_length=100)
    ASIN = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.IntegerField()
    book_url =models.URLField()
    publisher = models.CharField(max_length=200)
    publication_date = models.DateField()
    language = models.CharField(max_length=10)
    
    class meta:
        ordering ='publication_date'
    
    def __str__(self):
        return self.title    
    
class Movie(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=150)
    story_line = models.CharField(max_length=400)
    youtube_url = models.URLField()
    staring = models.CharField(max_length=200)
    poster_image = models.URLField()
    year_released = models.DateTimeField()
    
    class meta:
        ordering = 'year_released'
    
    def __str__(self):
        return self.title     
        
    
