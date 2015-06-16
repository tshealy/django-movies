import operator
from django.db.models import Avg, Count
from .models import Movie, Rater, Rating, Genre
from .forms import UserForm, RaterForm, RatingForm, EditForm, DeleteForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

def top_movies(request):
    print("DOES THIS WORK")
    # movies_query = Movie.objects.all()
    # movies_dict = {m: m.average_rating for m in movies_query if isinstance(m.average_rating, float)}
    # sorted_movies = sorted(movies_dict.items(), key=operator.itemgetter(1), reverse=True)
    # top_20_movies = sorted_movies[:20]
    # movies = [m[0] for m in top_20_movies]
    # return render(request, "moviebase/top_movies.html", {'movies': movies})
    movies = Movie.objects.annotate(avg_rating=Avg('rating__rating')).annotate(num_ratings=Count
        ('rating__rating')).filter(num_ratings__gt=30).order_by('-avg_rating')[:20]
    print("DOES THIS WORK")
    rated_movies = Movie.objects.annotate(avg_rating=Avg('rating__rating')).annotate(num_ratings=Count
        ('rating__rating')).order_by('-num_ratings')[:20]
    print("DOES THIS WORK")
    return render(request, "moviebase/top_movies.html",
                  {"movies": movies,
                  "rated_movies": rated_movies})

# def all_movies(request):
#     movies = Movie.objects.annotate(
#         rating_count=Count('rating'),
#         avg_rating=Avg('rating__rating'),
#     ).filter(rating_count__gte=10).order_by('-avg_rating')[:20]
#     return render(request, 'moviebase/all_movies.html', {"movies": movies})


def show_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    ratings = movie.rating_set.all()
    user_ratings = [rating.movie for rating in request.user.rater.rating_set.all()]
    rating_dict = {rating.movie: rating for rating in request.user.rater.rating_set.all()}
    if movie in user_ratings:
        user_rating = rating_dict[movie]
    else:
        user_rating = None
    rating_form = RatingForm()
    edit_form = EditForm()
    return render(request, "moviebase/show_movie.html",
                  {"movie": movie,
                   "ratings": ratings,
                   "rating_form": rating_form,
                   "user_rating": user_rating,
                   "edit_form": edit_form
                   })


def show_rater(request, rater_id):

    rater = Rater.objects.get(pk=rater_id)
    ratings = rater.rating_set.all()

    movies = Movie.objects.annotate(avg_rating=Avg('rating__rating')).annotate(num_ratings=Count
        ('rating__rating')).filter(num_ratings__gt=30).order_by('-avg_rating')
    movie_set = [rating.movie for rating in ratings]
    movies_not_seen = [movie for movie in movies if movie not in movie_set]

    return render(request,
                  "moviebase/rater.html",
                  {"rater": rater,
                   "ratings": ratings,
                   "movies_not_seen": movies_not_seen[:20]})


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

            # You must call authenticate before login.
            user = authenticate(username=user.username,
                                password=password)
            login(request, user)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Congratulations, {}, on creating your new account! You are now logged in.".format(
                    user.username))
            return redirect('top_movies')
    return render(request, "moviebase/register.html", {'user_form': user_form,
                                                   'rater_form': rater_form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/moviebase/')


def make_rating(request, movie_id):

   if request.method == 'POST':
       rating_form = RatingForm(data=request.POST)

       if rating_form.is_valid():
           movie = Movie.objects.get(pk=movie_id)
           rating = rating_form.save(commit=False)
           rating.rater = request.user.rater
           rating.movie = movie
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


def edit_rating(request, movie_id, rating_id):
    user_rating = Rating.objects.get(pk=rating_id)
    if request.method == 'POST':

        edit_form = EditForm(data=request.POST, instance = user_rating)

        if edit_form.is_valid():
            rating = edit_form.save(commit=False)
            rating.save()

            messages.add_message(
                request,
                messages.SUCCESS,
                "You have registered a review of {}".format(rating.movie)
            )
        return redirect('show_rater', request.user.rater.id)
    else:
        edit_form = EditForm(instance=user_rating)

    return render(request,
                  "moviebase/movie/{}.html".format(movie_id),
                  {'edit_form': edit_form})


def delete_rating(request, movie_id, rating_id):
    user_rating = Rating.objects.get(pk=rating_id)
    movie = user_rating.movie
    if request.method == 'POST':
        user_rating.delete()

        messages.add_message(
                request,
                messages.SUCCESS,
                "You have DELETED a review of {}".format(movie)
            )
        return redirect('show_rater', request.user.rater.id)
    else:
        delete_form = DeleteForm(instance=user_rating)

    return render(request,
                  "moviebase/movie/{}.html".format(movie_id),
                  {'delete_form': delete_form})