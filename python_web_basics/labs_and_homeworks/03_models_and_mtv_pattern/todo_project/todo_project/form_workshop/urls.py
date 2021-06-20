from django.urls import path

from todo_project.form_workshop.views import form, form_send

urlpatterns = [
    path('', form, name='show_form'),
    path('send/', form_send, name='form_send'),
]
