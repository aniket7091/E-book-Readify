from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Book
from .forms import BookForm
from django.shortcuts import render, get_object_or_404


from django.shortcuts import render
from .models import Book

def home(request):
    query = request.GET.get('q')
    if query:
        popular_books = Book.objects.filter(title__icontains=query)
    else:
        popular_books = Book.objects.all()
    return render(request, 'home.html', {'popular_books': popular_books, 'query': query})





def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_book')  # Replace with your home URL name
        else:
            print(form.errors)  # Debug: Check what’s going wrong
    else:
        form = BookForm()

    return render(request, 'upload_book.html', {'form': form})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})