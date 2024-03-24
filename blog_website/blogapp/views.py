from django.shortcuts import render,redirect
from .models import BlogPost,Category,CommentsPost
from .forms import CommentForm
from django.contrib import messages

# Create your views here.
def home_page_view(request):
    all_data=BlogPost.objects.all()
    context={
        "posts":all_data
    }
    response=render(request, "main/index.html",context)
    response.set_cookie("visitor", 'some server value')
    return response


def about_page_view(request):
    return render(request, "main/about.html")

def contact_page_view(request):
    return render(request, "main/contact.html")


def blog_details_view(request, blog_id):
    blog_post= BlogPost.objects.get(id=blog_id)
    categories= Category.objects.all()
    similar_posts= BlogPost.objects.filter(category=blog_post.category).exclude(id=blog_post.id)
    comment= CommentForm()
    comments = CommentsPost.objects.filter(comments=blog_post)
    print(request.COOKIES.get("visitor"))

    context= {
        "post": blog_post,
        "categories": categories,
        "similar_posts": similar_posts,
        "form":comment,
        "comments": comments
    }
    if request.method == "POST":
        form= CommentForm(request.POST)
        if form.is_valid():
            comment= form.save(commit=False)
            comment.comments= blog_post
            comment.save()
            messages.success(request, "Comment Added Successfully")
            return redirect("post_detail", blog_id=blog_post.id)

    return render(request, "main/post.html", context)

def posts_by_category(request, category_name):
    posts=BlogPost.objects.filter(category__name=category_name)
    context={
        "posts": posts
    }
    return render(request, "main/category_name.html", context)




