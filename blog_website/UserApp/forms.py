from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms





class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password1','password2']

class BlogPostForm(forms.Form):
    posts=forms.CharField(max_length=150,min_length=5,label='Posts',widget=forms.Textarea)


