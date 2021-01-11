from rest_framework import serializers
from book_master.models import Book, Purchase
from rest_framework import status


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'book_name', 'book_count', 'author']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)


class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)


class PurchaseSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()
    purchase_date = serializers.DateField()


class BorrowedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'book_name', 'author']