from django.shortcuts import render
from django.shortcuts import render

from movies.models import Movie
import requests
# Create your views here.
def action(request):
    movies = Movie.objects.filter(genre__contains="Action")
    print(movies)
    poster = []
    for i in movies:
     
     
        poster.append(fetch_poster(i.id))
        
    result = list(zip(movies,poster))
    context = {'result':result}
    return render(request,'genre/action.html',context)

def comedy(request):
    movies = Movie.objects.filter(genre__contains="Comedy")
    poster = []
    for i in movies:
        poster.append(fetch_poster(i.id))

    result = list(zip(movies,poster))
    context = {'result':result}
    return render(request,'genre/comedy.html',context)

def drama(request):
    movies = Movie.objects.filter(genre__contains="Drama")
    poster = []
    for i in movies:
        poster.append(fetch_poster(i.id))

    result = list(zip(movies,poster))
    context = {'result':result}
    return render(request,'genre/drama.html',context)

def thriller(request):
    movies = Movie.objects.filter(genre__contains="Thriller")
    poster = []
    for i in movies:
        poster.append(fetch_poster(i.id))

    result = list(zip(movies,poster))
    context = {'result':result}
    return render(request,'genre/thriller.html',context)


def adventure(request):
    movies = Movie.objects.filter(genre__contains="Adventure")
    poster = []
    for i in movies:
        poster.append(fetch_poster(i.id))

    result = list(zip(movies,poster))
    context = {'result':result}
    return render(request,'genre/adventure.html',context)


def romance(request):
    movies = Movie.objects.filter(genre__contains="Romance")
    poster = []
    for i in movies:
        poster.append(fetch_poster(i.id))

    result = list(zip(movies,poster))
    context = {'result':result}
    return render(request,'genre/romance.html',context)


def crime(request):
    movies = Movie.objects.filter(genre__contains="Crime")
    poster = []
    for i in movies:
        poster.append(fetch_poster(i.id))

    result = list(zip(movies,poster))
    context = {'result':result}
    return render(request,'genre/crime.html',context)


def sciencefiction(request):
    movies = Movie.objects.filter(genre__contains="ScienceFiction")
    poster = []
    for i in movies:
        poster.append(fetch_poster(i.id))

    result = list(zip(movies,poster))
    context = {'result':result}
    return render(request,'genre/sciencefiction.html',context)


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path