from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, SAFE_METHODS
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from .models import Book, Transaction
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        return [IsAdminUser()]

    @action(detail=True, methods=['post'])
    def checkout(self, request, pk=None):
        book = self.get_object()

        if book.available_copies < 1:
            return Response(
                {"error": "No copies available"},
                status=status.HTTP_400_BAD_REQUEST
            )

        Transaction.objects.create(
            user=request.user,
            book=book
        )

        book.available_copies -= 1
        book.save()

        return Response(
            {"message": "Book checked out successfully"},
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        book = self.get_object()

        try:
            transaction = Transaction.objects.get(
                user=request.user,
                book=book,
                returned=False
            )
        except Transaction.DoesNotExist:
            return Response(
                {"error": "No active transaction found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        transaction.returned = True
        transaction.return_date = timezone.now()
        transaction.save()

        book.available_copies += 1
        book.save()

        return Response(
            {"message": "Book returned successfully"},
            status=status.HTTP_200_OK
        )