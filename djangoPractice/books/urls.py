from django.urls import path
from . import views
from .views import BookDeleteAPIView, BookListCreateAPIView
urlpatterns = [
    path('', BookListCreateAPIView.as_view(), name='book_list_create'),
    path('delete/<id>/', BookDeleteAPIView.as_view(), name='delete_book'),
    path('delete-all/', DeleteAllBooksAPIView.as_view(), name='delete-all-books')
]