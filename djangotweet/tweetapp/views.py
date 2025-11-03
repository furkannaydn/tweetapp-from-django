from django.shortcuts import render

# Create your views here.

def listtweets(request):
    return render(request, 'tweetapp/listtweets.html')

def addtweets(request):
    return render(request, 'tweetapp/addtweets.html')