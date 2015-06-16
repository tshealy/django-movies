from django.contrib import admin
from .models import Rater, Movie, Rating, Genre


class RaterAdmin(admin.ModelAdmin):
    list_display = ['id', 'gender', 'age', 'postal_code']

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie', 'rating']

class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre']

admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Genre, GenreAdmin)
