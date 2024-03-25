from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Library
from .forms import StatusForm, LibraryForm
from catalog.models import Book


# Create your views here.
@login_required
def library_view(request):
    library = Library.objects.all()
    form = StatusForm()
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['status_field'] == 'ALL':
                library = Library.objects.all()
            else:
                library = Library.objects.filter(status=form.cleaned_data['status_field'])
        return render(request, 'library/library.html', {'library': library, 'form': form})
    return render(request, 'library/library.html', {'library': library, 'form': form})

@login_required
def book_tracker_view(request, book_slug):
    library = get_object_or_404(Library, book__slug=book_slug)
    progress = int(library.pages_read / library.book.page_count * 100)
    initial_data = {'status': library.status, 'pages_read': library.pages_read}
    if request.method == 'POST':
        form = LibraryForm(request.POST, instance=library)
        if form.is_valid():
            form.save()
        return redirect('library:tracker', book_slug=book_slug)
    else:
        form = LibraryForm(initial=initial_data)
    return render(request,
                  template_name='library/book_tracker.html',
                  context={'library': library, 'book': library.book, 'progress': progress, 'form': form}
                  )

@login_required
def add_book(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    # Library.objects.filter(book__slug=book_slug)
    if not Library.objects.filter(book=book).exists():
        Library.objects.create(owner=request.user, book=book)
    return redirect('library:library')
