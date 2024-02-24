from django.urls import path
from.views import home_page_view, about_page_view,contact_page_view

urlpatterns=[
    path('', home_page_view, name="home"),
    path('index/', about_page_view, name="about_page"),
    path('contact/', contact_page_view, name= "contact_page"),
    
]