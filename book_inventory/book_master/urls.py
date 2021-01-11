
from django.urls import path

from book_master.api import BookListAPI, BookDetail, LoginAPI, RegisterAPI, PurchaseAPI, BorrowedBookAPI


urlpatterns = [
    path('books/', BookListAPI.as_view(), name='Booklist'),
    path('book/<int:pk>/', BookDetail.as_view(), name='detail'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('purchase/', PurchaseAPI.as_view(), name='purchase'),
    path('borrowed-book/', BorrowedBookAPI.as_view(), name='borrowed')
    ]