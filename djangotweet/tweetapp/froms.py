from django import forms

class AddTweetForm(forms.Form):
   nickname_input=forms.CharField(label="Nickname", max_length=30)
   message_input=forms.CharField(label="Message", max_length=280, widget=forms.Textarea)
   