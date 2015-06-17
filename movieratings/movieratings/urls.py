"""movieratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from moviebase import views as moviebase_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^', include('django.contrib.auth.urls')),
    # url(r'^moviebase/all-movies/$', moviebase_views.all_movies, name="all_movies"),
    url(r'^moviebase/$', moviebase_views.top_movies, name="top_movies"),
    url(r'^moviebase/movie/(?P<movie_id>\d+)$', moviebase_views.show_movie, name="show_movie"),
    url(r'^moviebase/rater/(?P<rater_id>\d+)$', moviebase_views.show_rater, name="show_rater"),
    url(r'^moviebase/rater_history/(?P<rater_id>\d+)$', moviebase_views.rater_history, name="rater_history"),
    url(r'^moviebase/register/$', moviebase_views.user_register, name="user_register"),
    url(r'^moviebase/logout/$', moviebase_views.user_logout, name="logout"),
    url(r'^moviebase/rating/(?P<movie_id>\d+)$', moviebase_views.make_rating, name="make_rating"),
    url(r'^moviebase/edit_rating/(?P<movie_id>\d+)/(?P<rating_id>\d+)$', moviebase_views.edit_rating, name="edit_rating"),
    url(r'^moviebase/delete_rating/(?P<movie_id>\d+)/(?P<rating_id>\d+)$', moviebase_views.delete_rating, name="delete_rating"),
]