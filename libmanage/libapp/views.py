from email.policy import HTTP
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import *
from .forms import BookForm, CatForm

def index(request):
    if request.method == "POST":
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
            return HttpResponseRedirect('/')
        add_cat = CatForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()
            return HttpResponseRedirect('/')
    
    context = {
        'books': Book.objects.all(),
        'catigory': Catigory.objects.all(),
        'bookform': BookForm(),
        'catform': CatForm(),
        'allbooks': Book.objects.filter(active=True).count(),
        'solidbooks': Book.objects.filter(status='solid').count(),
        'rentalbooks': Book.objects.filter(status='rental').count(),
        'availablebooks': Book.objects.filter(status='available').count(),
        }
    return render(request, 'libapp/index.html', context)

def books(request):
    if request.method == "POST":
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_cat = CatForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()
            return HttpResponseRedirect('/')
    search = Book.objects.all()
    title = None
    
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)
    context = {
        'books': search,
        'catigory': Catigory.objects.all(),
        'catform': CatForm(),
        }
    return render(request, 'libapp/books.html', context)

def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        edit_book = BookForm(request.POST, request.FILES, instance=book_id)
        if edit_book.is_valid():
            edit_book.save()
            return HttpResponseRedirect('/')
    else:
        edit_book = BookForm(instance=book_id)
        
    context = {
        'edit_book': edit_book
        }
    return render(request, 'libapp/update.html', context)
    
def delete(request, id):
    book_id = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book_id.delete()
        return HttpResponseRedirect('/')
    return render(request, 'libapp/delete.html')