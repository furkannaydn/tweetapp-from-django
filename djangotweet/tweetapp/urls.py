from django.urls import path
from .import views

app_name = 'tweetapp'

urlpatterns = [
    path('listtweets/',views.listtweets, name='listtweets'),
    path('addtweets/',views.addtweets, name='addtweets'),
]
