from django.shortcuts import redirect, render
from . import models
from django.urls import reverse
from .froms import AddTweetForm
# Create your views here.

def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {'tweets': all_tweets}
    return render(request, 'tweetapp/listtweet.html', context=tweet_dict)

def addtweet(request):
    if request.method == "POST":
        nickname = request.POST.get("nickname")
        message = request.POST.get("message")
        models.Tweet.objects.create(nickname=nickname, message=message)
        return redirect(reverse('tweetapp:listtweet'))
    else:
        return render(request, 'tweetapp/addtweet.html')
    
def addtweetbyform(request):
    if request.method == "POST":
            print(request.POST)
            return redirect(reverse('tweetapp:listtweet'))
   
            return render(request, 'tweetapp/addtweetbyform.html', context={'form':form})
    else:
        form=AddTweetForm()
        return render(request, 'tweetapp/addtweetbyform.html', context={'form':form})