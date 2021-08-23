from django.urls import path
from .views import BookDetail, BookList,MovieDetail, MovieList 


urlpatterns = [
    path('books/',BookList.as_view(),name = 'book'),
    path('books/<int:pk>/', BookDetail.as_view() ,name ='singlebook'),
    path('movies/', MovieList.as_view(),name= 'movies'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name = 'singlemovie')
]