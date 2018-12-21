from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('title','image','content','status')

class UserLoginForm(forms.Form):
    username = forms.CharField(label='')
    password = forms.CharField(label='', widget=forms.PasswordInput)
