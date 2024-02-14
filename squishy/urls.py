
from django.urls import path
from . import views


app_name = "squishy"
urlpatterns = [
    path("", views.index, name="index"),
    path("pixels", views.pixels, name="pixel")
]