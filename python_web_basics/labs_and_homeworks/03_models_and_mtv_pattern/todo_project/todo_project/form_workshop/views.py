from django.http import HttpResponse
from django.shortcuts import render
from todo_project.form_workshop.forms import WorkshopForm

# Create your views here.


def form(request):
    context = {
        'form': WorkshopForm
    }

    return render(request, 'form_workshop/form.html', context)


def form_send(request):
    workshop_form = WorkshopForm(request.POST)
    if workshop_form.is_valid():
        fields = ['name', 'age', 'email', 'password', 'text']
        result = 'VALIDATION SUCCESS\n'

        for field in fields:
            result += f'{field}: {workshop_form.cleaned_data[field]}\n'
        return HttpResponse(result, content_type='text/plain')

    context = {
        'form': workshop_form
    }

    return render(request, 'form_workshop/form.html', context)
