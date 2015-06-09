from django.contrib import admin
from .models import Rater, Movie, Rating


class RaterAdmin(admin.ModelAdmin):
    list_display = ['id', 'gender', 'age', 'postal_code']

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre']

class RatingAdmin(admin.ModelAdmin):
    list_display = ['rating', 'timestamp']

admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
