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
