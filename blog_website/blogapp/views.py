from django.shortcuts import render
from .models import BlogPost
# Create your views here.
def home_page_view(request):

    all_data=BlogPost.objects.all()
    context={
        "posts":all_data
    }
    return render(request, "main/index.html",context)

def about_page_view(request):
    return render(request, "main/about.html")

def contact_page_view(request):
    return render(request, "main/contact.html")


def blog_details_view(request, blog_id):
    blog_post= BlogPost.objects.get(id=blog_id)
    context= {
        "post": blog_post
    }
    return render(request, "main/post.html", context)