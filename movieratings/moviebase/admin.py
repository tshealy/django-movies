from django.contrib import admin
from .models import Rater, Movie, Rating, Genre


class RaterAdmin(admin.ModelAdmin):
    list_display = ['id', 'gender', 'age', 'num_reviews', 'average_rating', 'postal_code']

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'average_rating']
    search_fields = ['title']

class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie', 'rating']
    fieldsets = [
        ('Rating information',  {'fields': ['rater', 'rating']}),
        ('Movie information',    {'fields': ['movie']}),
    ]
    list_filter = ['rater']

class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre']

admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Genre, GenreAdmin)


