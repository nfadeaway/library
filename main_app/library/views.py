from django.db.models import Q, Prefetch
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.core.cache import cache

from library.forms import AddAuthorForm, AddBookForm
from library.models import Book, Author
from library.utils import CommonDataMixin

# Create your views here.

class BooksListView(CommonDataMixin, ListView):
    model = Book
    template_name = 'library/books.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()
        queryset = super().get_queryset().prefetch_related('authors')
        if not query:
            cached_books = cache.get('books_list')
            if not cached_books:
                cached_books = queryset
                cache.set('books_list', cached_books, timeout=60 * 5)
            return cached_books
        return queryset.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(isbn__icontains=query) | Q(authors__surname__icontains=query)
        ).distinct()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        common_context = self.get_common_context(page_title='Книги', model=self.model)
        return dict(list(context.items()) + list(common_context.items()))


class AuthorsListView(CommonDataMixin, ListView):
    model = Author
    template_name = 'library/authors.html'
    context_object_name = 'authors'

    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()
        queryset = super().get_queryset().prefetch_related('books')
        if not query:
            cached_authors = cache.get('authors_list')
            if not cached_authors:
                cached_authors = queryset
                cache.set('authors_list', cached_authors, timeout=60 * 5)
            return cached_authors
        return queryset.filter(
            Q(surname__icontains=query)
        ).distinct()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        common_context = self.get_common_context(page_title='Авторы', model=self.model)
        return dict(list(context.items()) + list(common_context.items()))


class BookDetailView(CommonDataMixin, DetailView):
    model = Book
    template_name = 'library/book.html'
    pk_url_kwarg = 'book_id'
    context_object_name = 'book'

    def get_object(self, queryset=None):
        book_id = self.kwargs.get(self.pk_url_kwarg)
        cache_key = f'book_detail_{book_id}'
        cached_book = cache.get(cache_key)
        if not cached_book:
            cached_book = super().get_object(queryset)
            cache.set(cache_key, cached_book, timeout=60 * 10)
        return cached_book

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        common_context = self.get_common_context(model=self.model)
        return dict(list(context.items()) + list(common_context.items()))


class AuthorDetailView(CommonDataMixin, DetailView):
    model = Author
    template_name = 'library/author.html'
    pk_url_kwarg = 'author_id'
    context_object_name = 'author'

    def get_object(self, queryset=None):
        author_id = self.kwargs.get(self.pk_url_kwarg)
        cache_key = f'author_detail_{author_id}'
        cached_author = cache.get(cache_key)
        if not cached_author:
            cached_author = super().get_object(queryset)
            cache.set(cache_key, cached_author, timeout=60 * 10)
        return cached_author

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        common_context = self.get_common_context(model=self.model)
        return dict(list(context.items()) + list(common_context.items()))


class AddBookView(CommonDataMixin, CreateView):
    model = Author
    form_class = AddBookForm
    template_name = 'library/add_item.html'
    success_url = reverse_lazy('books')

    def form_valid(self, form):
        book = form.save()
        cache.delete('books_list')
        return redirect(reverse('book', kwargs={'book_id': book.pk}))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        common_context = self.get_common_context(page_title='Добавить книгу')
        return dict(list(context.items()) + list(common_context.items()))


class AddAuthorView(CommonDataMixin, CreateView):
    model = Author
    form_class = AddAuthorForm
    template_name = 'library/add_item.html'
    success_url = reverse_lazy('authors')

    def form_valid(self, form):
        author = form.save()
        cache.delete('authors_list')
        return redirect(reverse('author', kwargs={'author_id': author.pk}))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        common_context = self.get_common_context(page_title='Добавить автора')
        return dict(list(context.items()) + list(common_context.items()))


class DeleteBookView(View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        book.delete()
        cache.delete('books_list')
        return redirect('books')


class DeleteAuthorView(View):
    def post(self, request, author_id):
        author = get_object_or_404(Author, pk=author_id)
        author.delete()
        cache.delete('authors_list')
        return redirect('authors')


def page404(request, exception):
    return HttpResponseNotFound('Страница не найдена')
