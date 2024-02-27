from django.urls import path
from.views import home_page_view, about_page_view,contact_page_view,blog_details_view

urlpatterns=[
    path('', home_page_view, name="home"),
    path('index/', about_page_view, name="about_page"),
    path('contact/', contact_page_view, name= "contact_page"),
    path('post/<int:blog_id>/', blog_details_view, name="post_detail")
    
]