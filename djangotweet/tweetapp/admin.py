from django.contrib import admin
from . import models
from django.urls import path, include
from tweetapp.models import Tweet


class TweetAdmin(admin.ModelAdmin):
    fieldsets =[
        ('Message Group', {'fields': ['message']}),
        ('Nick Group', {'fields': ['nickname']}),
    ]
    
    #fields=['nickname', 'message']

# Register your models here.
admin.site.register(Tweet, TweetAdmin)
