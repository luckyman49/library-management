from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# -------------------------
# Book Model
# -------------------------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    copies_available = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)

    def clean(self):
        if self.available_copies < 0:
            raise ValidationError("Available copies cannot be negative.")

        if self.available_copies > self.copies_available:
            raise ValidationError("Available copies cannot exceed total copies.")

    def __str__(self):
        return self.title


# -------------------------
# Transaction Model
# -------------------------
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"