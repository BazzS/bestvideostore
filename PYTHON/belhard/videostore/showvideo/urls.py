from django.urls import path
from . import views

urlpatterns = [
    path("123/", views.hello),
    path("456/", views.world),
]