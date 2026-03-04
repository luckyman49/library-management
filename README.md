I created a Transaction model to track borrowing history, prevent duplicate checkouts, and maintain proper record of return dates instead of modifying the Book model directly.

# 📚 Library Management API

A Django REST Framework API for managing books and tracking user transactions (checkout and return).

---

## 🚀 Features Implemented

- Django project setup
- Book model (CRUD operations)
- Transaction model (track checkouts & returns)
- Token Authentication
- Permission control:
  - Authenticated users can view books
  - Only admins can create, update, or delete books
- Custom endpoints:
  - Checkout a book
  - Return a book

---

 # user Authentication

This API uses Token Authentication.

Users must log in and include a token in the request header:



Today's Work Summary

Continued building the backend API for the Library Management system.

Focused on improving existing endpoints and adding new functionalities for book management.

Implemented additional test cases to ensure reliability of checkout and return operations.

Encountered and resolved several challenges related to database relationships and test failures.

Refined serializers and ModelViewSet logic for efficient CRUD operations.

Documented changes and ensured code readability for future submissions.

Challenges Faced:

Handling edge cases in book checkout and return.

Debugging test failures caused by relational constraints.

Ensuring proper validation in serializers for data integrity.
