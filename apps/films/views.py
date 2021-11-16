from django.shortcuts import render
from apps.films.models import Film

# Create your views here.
def film_view(request):
    films = Film.objects.all()
    return render(request, 'films/index.html', {'films': films})