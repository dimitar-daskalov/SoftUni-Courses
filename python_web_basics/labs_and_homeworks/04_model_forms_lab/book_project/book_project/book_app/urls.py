from django.urls import path

from book_project.book_app.views import index, create, edit

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create_book'),
    path('edit/<int:pk>', edit, name='edit_book'),
]
