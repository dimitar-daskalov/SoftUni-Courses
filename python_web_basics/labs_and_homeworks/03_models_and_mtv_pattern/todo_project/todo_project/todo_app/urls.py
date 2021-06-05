from django.urls import path

from todo_project.todo_app import views

urlpatterns = [
    path('', views.index)
]
