# from django.http import JsonResponse
# from django.shortcuts import render

# from watchlist.models import Movie

# # Create your views here.

# def movie_list(request):
#     movies = Movie.objects.all()
#     # print(movies.values())
#     data = {
#         'movie': list(movies.values())
#     }

#     return JsonResponse(data)


# def movie_details(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         'name': movie.name,
#         'description': movie.description,
#         'active': movie.active
#     }

#     return JsonResponse(data)