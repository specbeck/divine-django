from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import default_storage
from django import forms
from PIL import Image
from django.urls import reverse
import cv2, os
from .models import Memory
class ImageUpload(forms.Form):
    image = forms.ImageField(label="Upload an image")
    alt = forms.CharField(label="Enter alt text")

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
            memory = Memory(image=image, description=alt)
            memory.save()
            return HttpResponseRedirect(request, reverse("index"))
        else:
            return render(request, "gallery/create.html", {
                "form" : form
            })
    return render(request, "gallery/create.html", {
        "form" : ImageUpload()
    })
