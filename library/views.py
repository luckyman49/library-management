from django.utils import timezone
from django.db import transaction

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from .models import Book, Transaction
from .serializers import BookSerializer, TransactionSerializer
from .permissions import IsAdminOrReadOnly, IsAuthenticatedUser   # <-- use our new rules


# -------------------------
# Transaction ViewSet
# -------------------------
class TransactionViewSet(ReadOnlyModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticatedUser]   # only logged-in users

    def get_queryset(self):
        # Only return transactions for the logged-in user
        return Transaction.objects.filter(user=self.request.user)


# -------------------------
# Book ViewSet
# -------------------------
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]   # admins can add/delete, others read-only

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['available_copies']
    search_fields = ['title', 'author']
    ordering_fields = ['published_date', 'title']

    # -------------------------
    # Checkout Book
    # -------------------------
    @action(detail=True, methods=['post'])
    @transaction.atomic
    def checkout(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

        book = self.get_object()

        existing_transaction = Transaction.objects.filter(
            user=request.user,
            book=book,
            returned=False
        ).exists()

        if existing_transaction:
            return Response(
                {"error": "You already checked out this book"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if book.available_copies < 1:
            return Response(
                {"error": "No copies available"},
                status=status.HTTP_400_BAD_REQUEST
            )

        Transaction.objects.create(user=request.user, book=book)
        book.available_copies -= 1
        book.save()

        return Response({"message": "Book checked out successfully"}, status=status.HTTP_200_OK)

    # -------------------------
    # Return Book
    # -------------------------
    @action(detail=True, methods=['post'])
    @transaction.atomic
    def return_book(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

        book = self.get_object()

        try:
            transaction_record = Transaction.objects.get(
                user=request.user,
                book=book,
                returned=False
            )
        except Transaction.DoesNotExist:
            return Response(
                {"error": "You don't have this book checked out"},
                status=status.HTTP_400_BAD_REQUEST
            )

        transaction_record.returned = True
        transaction_record.return_date = timezone.now()
        transaction_record.save()

        book.available_copies += 1
        book.save()

        return Response({"message": "Book returned successfully"}, status=status.HTTP_200_OK)
