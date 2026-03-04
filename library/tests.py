from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book


class LibraryAPITest(APITestCase):

    def setUp(self):
        # Create normal user
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

        # Create admin user
        self.admin = User.objects.create_superuser(
            username="admin",
            password="admin123",
            email="admin@test.com"
        )

        # Create book
        self.book = Book.objects.create(
            title="Python Basics",
            author="John Doe",
            isbn="1234567890123",
            published_date="2023-01-01",
            copies_available=5,
            available_copies=5
        )

    # -------------------------
    # Test Book List
    # -------------------------
    def test_book_list_authenticated(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # -------------------------
    # Test Checkout
    # -------------------------
    def test_checkout_book(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.post(f"/api/books/{self.book.id}/checkout/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book.refresh_from_db()
        self.assertEqual(self.book.available_copies, 4)

    # -------------------------
    # Prevent Duplicate Checkout
    # -------------------------
    def test_duplicate_checkout(self):
        self.client.login(username="testuser", password="password123")

        # First checkout
        self.client.post(f"/api/books/{self.book.id}/checkout/")

        # Second checkout attempt
        response = self.client.post(f"/api/books/{self.book.id}/checkout/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # -------------------------
    # Test Return Book
    # -------------------------
    def test_return_book(self):
        self.client.login(username="testuser", password="password123")

        # Checkout first
        self.client.post(f"/api/books/{self.book.id}/checkout/")

        # Then return
        response = self.client.post(f"/api/books/{self.book.id}/return_book/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book.refresh_from_db()
        self.assertEqual(self.book.available_copies, 5)

    # -------------------------
    # Admin Only Create Book
    # -------------------------
    def test_non_admin_cannot_create_book(self):
        self.client.login(username="testuser", password="password123")

        response = self.client.post("/api/books/", {
            "title": "New Book",
            "author": "Someone",
            "isbn": "9999999999999",
            "published_date": "2024-01-01",
            "copies_available": 3,
            "available_copies": 3
        })

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)