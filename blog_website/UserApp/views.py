from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blogapp.forms import BlogForm, CommentForm
from blogapp.models import BlogPost
# Create your views here.



def register_page(request):
    cart=request.POST.get('cart')
    request.session['cart_items']='Some cart information'
    form=UserRegisterForm()
    context={
        "form":form
    }
    if request.method == 'POST':
        form_data= UserRegisterForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"USER ACCOUNT CREATED SUCCESSFULLY")
            return redirect("user-login")
    return render(request,"Accounts/register.html" ,context)

# def signup_page(request):   
#     return render(request, "Accounts/signup.html")

@login_required
def add_blog_post(request):
    cart_data=request.session.get('cart_items')
    print(cart_data)
    user=request.user
    post_form= BlogForm()
    context={
        "form": post_form,
        'cart':cart_data
    }
    if request.method == "POST":
        form=BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form_data=form.save(commit=False)
            form_data.author=user
            form_data.save()
            return redirect('home')

    return render(request, "posts/add_post.html",context)


# def add_comment(request):
#     comments_form=CommentForm()
#     context={
#         "commentform":comments_form
#     }
#     if request.method =="POST":
#         comment=CommentForm(request.POST)
#         if comment.is_valid():
#             comment.save()
#             return redirect('home')
#     return render(request, "posts/add_comment.html",context )



@login_required
def user_profile(request):
    posts=BlogPost.objects.filter(author=request.user)
    cart=request.session.get('cart_items')
    context={
        "cart":cart,
        'user_posts': posts,
    }
  
    return render (request,"Accounts/profile.html", context)

@login_required
def home_page(request):
     return render (request,"Accounts/homepage.html")


def logout_confirm(request):
    return render (request,"Accounts/logout_confirm.html")


