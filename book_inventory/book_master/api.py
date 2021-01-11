from django.contrib.auth.models import User
from book_master.models import Book, Purchase
from book_master.serializers import BookListSerializer, LoginSerializer, RegisterSerializer, PurchaseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate


class BookListAPI(generics.ListCreateAPIView):
    queryset = Book.objects.filter(status=True)
    serializer_class = BookListSerializer

class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.filter(status=True)
    serializer_class = BookListSerializer


class LoginAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data['email']
            password = serializer.data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                return Response("User is logged in")
            else:
                return Response("User is not logged in")


class RegisterAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data['name']
            email = serializer.data['email']
            password = serializer.data['password']
            user = User.objects.filter(username=email)
            if user:
                return Response("User already exist")
            user = User.objects.create(first_name=name, email=email, username=email, password=password)
            return Response("User created succesfully")


class PurchaseAPI(APIView):
    def post(self, request):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            book_id =serializer.data['book_id']
            purchase_date = serializer.data['purchase_date']
            book = Book.objects.filter(id = book_id)
            if not book:
                return Response("Wrong Book id selected")
            if not book.book_count:
                return Response("Book is not available")
            Purchase.objects.create(
                book=book,
                user=request.user,
                purchase_date=purchase_date
            )
            book.book_count -= 1
            book.save()
            return Response("Book Purchased")


class BorrowedBookAPI(APIView):
    def get(self, request):
        user = request.user
        purchased_book = Purchase.objects.filter(user=request.user)
        book_detail = []
        if not purchased_book:
            return Response("No books Purchased")
        for item in purchased_book:
            dict = {
                "book_name" : item.book.book_name,
                "purchased_date": item.purchase_date
            }
            book_detail.append(dict)

        return Response(book_detail)