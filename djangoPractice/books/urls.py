from django.urls import path
from . import views
from .views import BookDeleteAPIView, BookListCreateAPIView, DeleteAllBooksAPIView, CreateUserAPIView, UserDetailAPIView
urlpatterns = [
    #books api
    path('', BookListCreateAPIView.as_view(), name='book_list_create'),
    path('delete/<id>/', BookDeleteAPIView.as_view(), name='delete_book'),
    path('delete-all/', DeleteAllBooksAPIView.as_view(), name='delete-all-books'),
    
    #users api
    path('user/', CreateUserAPIView.as_view(), name='user'),
    path('user/<int:id>/', UserDetailAPIView.as_view(), name='user_detail'),
]