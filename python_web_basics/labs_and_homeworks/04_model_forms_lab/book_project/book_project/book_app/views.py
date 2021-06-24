from django.shortcuts import render, redirect
from book_project.book_app.forms import BookForm
from book_project.book_app.models import Book


# Create your views here.


def index(request):
    books = sorted(Book.objects.all(), key=lambda x: x.id)
    context = {
        'books': books
    }

    return render(request, 'templates/index.html', context)


def create(request):
    if request.method == 'GET':
        form = BookForm()
        context = {
            'form': form
        }

        return render(request, 'templates/create.html', context)

    else:
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'form': form
        }

        return render(request, 'templates/create.html', context)


def edit(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'GET':
        form = BookForm(initial=book.__dict__)

        context = {
            'form': form
        }

        return render(request, 'templates/edit.html', context)

    else:
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'form': form
        }

        return render(request, 'templates/edit.html', context)
