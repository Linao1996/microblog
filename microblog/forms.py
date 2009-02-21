from django import forms

class PostEntryForm(forms.Form):
    content = forms.CharField(max_length=250)

class FollowForm(forms.Form):
    users = forms.CharField(max_length=200)
