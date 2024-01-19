from django.shortcuts import render
from django.core.files.storage import default_storage
from django import forms
from PIL import Image
import cv2, os
class ImageUpload(forms.Form):
    image = forms.ImageField(label="Upload an image")
    alt = forms.CharField(label="Enter alt text")


# Create your views here.
def index(request):
    return render(request, "gallery/index.html")

def create(request):
    if request.method == "POST":
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            
            image = request.FILES["image"]
            alt = request.POST.get("alt")
            image_name = default_storage.save(image.name, image)
            return render(request, "gallery/index.html", {
                "image" : default_storage.url(image_name),
                "alt" : alt
            })
        else:
            return render(request, "gallery/create.html", {
                "form" : form
            })
    return render(request, "gallery/create.html", {
        "form" : ImageUpload()
    })
