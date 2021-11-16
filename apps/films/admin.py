from django.contrib import admin
from apps.films.models import Film, FilmImage

# Register your models here.
admin.site.register(Film)
admin.site.register(FilmImage)