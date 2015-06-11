from django.shortcuts import render

# Create your views here.
from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from .models import Rating
from .models import Rater
from collections import OrderedDict
import operator

def top_movies(request):
    movies_query = Movie.objects.all()
    movies_dict = {m: m.average_rating for m in movies_query if isinstance(m.average_rating, float)}
    sorted_movies = sorted(movies_dict.items(), key=operator.itemgetter(1), reverse=True)
    top_20_movies = sorted_movies[:20]
    movies = [m[0] for m in top_20_movies]
    # top_rated_movies = OrderedDict(sorted(movies_query_dict.items(), key=lambda x: x[1]))[:-20]
    return render(request, "moviebase/top_movies.html", {'movies': movies})

def show_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    ratings = movie.rating_set.all()
    return render(request, "moviebase/show_movie.html",
                  {"movie": movie,
                   "ratings": ratings})
#
def show_rater(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    ratings = rater.rating_set.all()
    return render(request,
                  "moviebase/show_rater.html",
                  {"rater": rater,
                   "ratings": ratings})