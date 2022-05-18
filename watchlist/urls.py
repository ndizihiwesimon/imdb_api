from django.urls import path

from watchlist.views import movie_list

urlpatterns = [
    path('list/', movie_list, name='movie-list'),
]

