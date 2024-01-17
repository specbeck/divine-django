from django.shortcuts import render

app_name = "gallery"
# Create your views here.
def index(request):
    return render(request, "gallery/index.html")