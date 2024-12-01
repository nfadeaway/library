from django.urls import path, include

from library.views import BooksListView, AuthorsListView, BookDetailView, AuthorDetailView, \
    AddAuthorView, AddBookView, DeleteBookView, DeleteAuthorView

urlpatterns = [
    path('', BooksListView.as_view(), name="books"),
    path('select2/', include('django_select2.urls')),
    path('books/<int:book_id>/', BookDetailView.as_view(), name="book"),
    path('books/<int:book_id>/delete/', DeleteBookView.as_view(), name='delete_book'),
    path('authors/', AuthorsListView.as_view(), name="authors"),
    path('authors/<int:author_id>/', AuthorDetailView.as_view(), name="author"),
    path('authors/<int:author_id>/delete', DeleteAuthorView.as_view(), name="delete_author"),
    path('addbook/', AddBookView.as_view(), name="add_book"),
    path('addauthor/', AddAuthorView.as_view(), name="add_author"),
]
