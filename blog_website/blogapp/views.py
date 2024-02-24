from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request, "main/index.html")

def about_page_view(request):
    return render(request, "main/about.html")

def contact_page_view(request):
    return render(request, "main/contact.html")