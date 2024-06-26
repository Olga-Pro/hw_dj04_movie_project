from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm

# Create your views here.
def home(request):
    return render(request, 'films/home.html')


def add_film(request):
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FilmForm()
    return render(request, 'films/add_film.html', {'form': form})

def home(request):
    films = Film.objects.all()
    return render(request, 'films/home.html', {'films': films})