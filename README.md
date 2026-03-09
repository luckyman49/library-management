 Library Management API
A Django REST Framework API for managing books and tracking user transactions (checkout and return).

 Features Implemented
Django project setup with REST Framework

Book model for CRUD operations

Transaction model to track checkouts & returns

Prevents duplicate checkouts

Maintains proper record of return dates

Token Authentication (JWT)

Permission control:

Authenticated users can view books

Only admins can create, update, or delete books

Custom endpoints:

Checkout a book

Return a book

 Development Process
Started by setting up the Django project and creating the Book model for basic CRUD operations.

Implemented JWT authentication so users can log in and securely access endpoints.

Designed a Transaction model instead of modifying the Book model directly, to keep borrowing history separate and enforce rules like preventing duplicate checkouts.

Added custom endpoints for checkout and return, ensuring proper validation and updating transaction records.

Applied permissions so only admins can manage books, while regular users can borrow and return.

Wrote test cases to cover edge cases and confirm reliability of checkout/return logic.

Refined serializers and viewsets for clean, efficient API responses.

 Usage Flow
Login → Obtain access and refresh tokens.

Refresh token → Renew access when expired.

List books → View all available books.

Book details → Get information about a single book.

Checkout → Borrow a book.

Return → Return a borrowed book.

Transactions → View borrowing history.

 Tech Stack
Backend: Django, Django REST Framework

Authentication: JWT (SimpleJWT)

Database: SQLite (can be swapped for PostgreSQL)

Deployment: PythonAnywhere

Testing: Postman, Django test framework

 Challenges & Solutions
Duplicate checkouts: Solved by validating transactions before creating new ones.

Return logic: Ensured proper return dates are recorded in the Transaction model.

Relational constraints: Debugged foreign key relationships and refined serializers.

Test failures: Added custom test cases to handle edge cases and confirm data integrity.

 Summary
This API demonstrates secure authentication, book management, and transaction tracking. By separating book data from transaction history, it ensures clean design, prevents misuse, and maintains accurate records of borrowing and returning.