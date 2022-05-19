from django.urls import path

from watchlist.api.views import MovieListAV, MovieDetailsAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailsAV.as_view(), name='movie-details'),
]
