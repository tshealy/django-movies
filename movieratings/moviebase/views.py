# Create your views here.
from django.db.models import Count, Avg
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Movie
from .models import Rating
from .models import Rater
import operator

from .forms import UserForm, RaterForm, RatingForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def top_movies(request):
    movies_query = Movie.objects.all()
    movies_dict = {m: m.average_rating for m in movies_query if isinstance(m.average_rating, float)}
    sorted_movies = sorted(movies_dict.items(), key=operator.itemgetter(1), reverse=True)
    top_20_movies = sorted_movies[:20]
    movies = [m[0] for m in top_20_movies]
    return render(request, "moviebase/top_movies.html", {'movies': movies})


def all_movies(request):
    movies = Movie.objects.annotate(
        rating_count=Count('rating'),
        avg_rating=Avg('rating__rating'),
    ).filter(rating_count__gte=10).order_by('-avg_rating')[:20]
    return render(request, 'moviebase/all_movies.html', {"movies": movies})

def show_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    ratings = movie.rating_set.all()
    return render(request, "moviebase/show_movie.html",
                  {"movie": movie,
                   "ratings": ratings})

def show_rater(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    ratings = rater.rating_set.all()
    return render(request,
                  "moviebase/show_rater.html",
                  {"rater": rater,
                   "ratings": ratings})

def user_register(request):
    if request.method == "GET":
        user_form = UserForm()
        rater_form = RaterForm()
    elif request.method == "POST":
        user_form = UserForm(request.POST)
        rater_form = RaterForm(request.POST)
        if user_form.is_valid() and rater_form.is_valid():
            user = user_form.save()
            profile = rater_form.save(commit=False)
            profile.user = user
            profile.save()

            password = user.password
            # The form doesn't know to call this special method on user.
            user.set_password(password)
            user.save()

            # You must call authenticate before login. :(
            user = authenticate(username=user.username,
                                password=password)
            login(request, user)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Congratulations, {}, on creating your new account! You are now logged in.".format(
                    user.username))
            return redirect('all_movies')
    return render(request, "moviebase/register.html", {'user_form': user_form,
                                                   'rater_form': rater_form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/moviebase/top-movies/')


def make_rating(request):

   if request.method == 'POST':
       rating_form = RatingForm(data=request.POST)

       if rating_form.is_valid():
           rating = rating_form.save()
           rating.save()

           messages.add_message(
               request,
               messages.SUCCESS,
               "You have registered a review of {}".format(rating.movie)
           )
           return redirect('/moviebase/rater/{}'.format(request.user.rater.id))

   else:
       rating_form = RatingForm()

   return render(request,
                 "moviebase/rating.html",
                 {'rating_form': rating_form})