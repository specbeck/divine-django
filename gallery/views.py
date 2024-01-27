from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from .models import Memory
class ImageUpload(forms.Form):
    image = forms.ImageField(label="Upload an image")
    alt = forms.CharField(label="Enter alt text depicting the image")
    name = forms.CharField(label="Enter your name")

# Create your views here.
def index(request):
    memories = Memory.objects.all()
    return render(request, "gallery/index.html", {
        "memories": memories
    })

def create(request):
    if request.method == "POST":
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES["image"]
            alt = request.POST.get("alt")   
            name = request.POST.get("name")
            memory = Memory(image=image, description=alt, poster=name)
            memory.save()
            return HttpResponseRedirect(reverse("gallery:index"))
        else:
            return render(request, "gallery/create.html", {
                "form" : form
            })
    return render(request, "gallery/create.html", {
        "form" : ImageUpload()
    })
