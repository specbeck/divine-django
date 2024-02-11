from django.urls import path

from . import views

app_name = "leveling"

urlpatterns = [
    path("", views.index, name="index")
]