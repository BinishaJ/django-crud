from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.IndexView.as_view(), name="index"),
    path("add",views.AddView.as_view(), name="add"),
    path("edit/<int:id>",views.EditView.as_view(), name="edit"),
    path("delete/<int:id>",views.DeleteView.as_view(), name="delete"),
]