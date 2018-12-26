from django import forms
from .models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('title','image','content','status')

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):                                       ##remove the help txt
		super(UserRegistrationForm, self).__init__(*args, **kwargs)

		for fieldname in ['username', 'password', 'confirm_password']:         ##remove the help txt
			self.fields[fieldname].help_text = None

	password = forms.CharField(widget=forms.PasswordInput(attrs ={'placeholder':'enter password here..'}))
	confirm_password=forms.CharField(widget=forms.PasswordInput(attrs ={'placeholder':'enter password here..'}))
	class Meta:
		model=User
		fields=('username','first_name','last_name','email')

	def cleam_confirm_password(self):
		password=self.cleaned_data.get('password')
		confirm_password=self.cleaned_data.get('confirm_password')
		if password !=confirm_password:
			raise forms.ValidationError('Pasword Mismatch')
		return confirm_password	