from django.urls import path
from . import views

urlpatterns = [
    path("123/", views.hello),
    path("456/", views.world, name="main_page"),
    path("comment/<int:id>/", views.accept_comment),
    path("one_video/<int:id>/", views.one_video),
]