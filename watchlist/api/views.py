from watchlist.models import Movie

def movie_list(request):
    movies = Movie.objects.all()