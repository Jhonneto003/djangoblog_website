from  django.urls import path
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetDoneView,PasswordResetCompleteView,PasswordResetConfirmView,PasswordResetView
from .views import register_page,logout_confirm,user_profile,home_page,add_blog_post


urlpatterns=[
    path('register/',register_page, name="create-account"),
    path('login/',LoginView.as_view(template_name="Accounts/login.html"),name="user-login"),
    path('logout/',LogoutView.as_view(template_name="Accounts/logout.html"),name="user-logout"),
    path('confirm-logout/',logout_confirm, name="logout-confirm"),
    path('profile/',user_profile,name="profile"),
    path('homepage/',home_page,name="home-page"),
    path('add-post/',add_blog_post, name="add-blog-post"),
    # path('reset_password/',PasswordResetView.as_view(template_name='Accounts/password_reset.html'),name="password-reset"),
    # path('reset/done/',PasswordResetCompleteView.as_view(template_name="Accounts/reset_complete.html"),name="reset_complete"),
    # path('password_reset/done/',PasswordResetDoneView.as_view(template_name="Accounts/password_reset_done.html"),name="password_reset_done"),
    # path('reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="Accounts/reset.html"),name="password_reset_confirm"),

]