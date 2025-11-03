from django.shortcuts import render
from . import models

# Create your views here.

def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {'tweets': all_tweets}
    return render(request, 'tweetapp/listtweet.html', context=tweet_dict)

def addtweet(request):
    if request.method == "POST":
        nickname = request.POST.get("nickname")
        message = request.POST.get("message")
        print(f"Nickname: {nickname}, Message: {message}")

    return render(request, 'tweetapp/addtweet.html') 