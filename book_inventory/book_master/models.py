from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_count = models.IntegerField()
    author = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.book_name


class Purchase(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateField()

    def __str__(self):
        return self.book.book_name
