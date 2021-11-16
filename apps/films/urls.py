from django.urls import path
from apps.films.views import film_view


urlpatterns = [
    path('', film_view, name = 'film_index')
]