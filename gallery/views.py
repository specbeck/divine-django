from django.shortcuts import render
from django.core.files.storage import default_storage
from django import forms
from PIL import Image
import cv2, os
class ImageUpload(forms.Form):
    image = forms.FileField(label="Upload an image")
    alt = forms.CharField(label="Enter alt text")


# Create your views here.
def index(request):
    return render(request, "gallery/index.html")

def create(request):
    if request.method == "POST":
        image = request.POST.get("image")
        alt = request.POST.get("alt")
        dir = "gallery/static/images/"
        file = cv2.imread(image)
        os.chdir(dir)
        cv2.imwrite(image, file)
        # filename = f"images/{image}"
        # default_storage.save(image, image)
        return render(request, "gallery/index.html", {
            "image" : image,
            "alt" : alt
        })
    return render(request, "gallery/create.html", {
        "image" : ImageUpload()
    })
