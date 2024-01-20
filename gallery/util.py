import cv2, os

def handle_uploaded_file(f):
    with open("gallery/static/images", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            