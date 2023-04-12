from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request,'advtempapp/home.html')



def movie_view(request):
    return render(request,'advtempapp/movie.html')

def sports_view(request):
    return render(request,'advtempapp/sports.html')

def politics_view(request):
    return render(request,'advtempapp/politics.html')