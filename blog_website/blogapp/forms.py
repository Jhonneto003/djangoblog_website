from django import forms
from .models import BlogPost, CommentsPost



class BlogForm(forms.ModelForm):
    class Meta:
        model= BlogPost
        fields= ['title','description','content','thumbnail','category','tags']
        widgets={
            "title": forms.TextInput(attrs={'class':'form-control mr-0 ml-auto'}),
            "description": forms.Textarea(attrs={'class':'form-control mr-0 ml-auto'}),
            "content": forms.Textarea(attrs={'class':'form-control mr-0 ml-auto'}),
            "category": forms.Select(attrs={'class':'form-control mr-0 ml-auto'}),
            "tags": forms.SelectMultiple(attrs={'class':'form-control mr-0 ml-auto'}),

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=CommentsPost
        fields= ['name', 'email', 'content']
        widgets={
            "name": forms.TextInput(attrs={'class':'form-control mr-0 ml-auto'}),
            "email": forms.EmailInput(attrs={'class':'form-control mr-0 ml-auto'}),
            "content":forms.Textarea(attrs={'class':'form-control mr-0 ml-auto'}),
            
        }