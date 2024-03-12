from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.



def register_page(request):
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
def user_profile(request):
    return render (request,"Accounts/profile.html")

@login_required
def home_page(request):
     return render (request,"Accounts/homepage.html")


def logout_confirm(request):
    return render (request,"Accounts/logout_confirm.html")


