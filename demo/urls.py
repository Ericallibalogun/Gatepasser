from django.urls import path

from demo import views

urlpatterns = [
    path("home",views.index),
    path("about",views.about),
]