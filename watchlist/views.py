from django.shortcuts import render
import requests



# Create your views here.



def home(request):
    response = requests.get('https://api.themoviedb.org/3/movie/343611?api_key=aea54ab4ea8fe9b77c0c89fa9776fcf8&append_to_response=videos')
    moviedata = response.json()
    data = moviedata['videos']['results']
    return render(request,'home.html',{
        'overview' :moviedata['overview'],
        'homepage' :moviedata['homepage'],
        'videos' : data

    })

