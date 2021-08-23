from rest_framework import serializers
from.models import Movie,Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 
                  'title', 
                  'category', 
                  'ASIN', 
                  'language', 
                  'price',
                  'pages',
                  'Author',
                  'book_url',
                  'publisher',
                  'publication_date',
                  'language',
                  
        )


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 
                  'title', 
                  'category', 
                  'story_line', 
                  'youtube_url', 
                  'staring',
                  'year_released',
                  'poster_image',
                
                  
        )

