from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("book/<int:notebook_id>/", views.notebook, name="notebook"),
    path("<int:note_id>/", views.note, name="note"),
]
