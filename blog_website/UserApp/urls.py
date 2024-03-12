from  django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import register_page,logout_confirm,user_profile,home_page


urlpatterns=[
    path('register/',register_page, name="create-account"),
    path('login/',LoginView.as_view(template_name="Accounts/login.html"),name="user-login"),
    path('logout/',LogoutView.as_view(template_name="Accounts/logout.html"),name="user-logout"),
    path('confirm/logout/',logout_confirm, name="logout-confirm"),
    path('/profile/',user_profile,name="profile"),
    path('homepage/',home_page,name="home-page")
]