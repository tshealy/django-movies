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
    url(r'^moviebase/all-movies/$', moviebase_views.all_movies, name="all_movies"),
    url(r'^moviebase/top-movies/$', moviebase_views.top_movies, name="top_movies"),
    url(r'^moviebase/movie/(?P<movie_id>\d+)$', moviebase_views.show_movie, name="show_movie"),
    url(r'^moviebase/rater/(?P<rater_id>\d+)$', moviebase_views.show_rater, name="show_rater")
]
