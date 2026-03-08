from rest_framework.routers import DefaultRouter
from .views import BookViewSet, TransactionViewSet

router = DefaultRouter()

router.register(r'books', BookViewSet)
router.register(r'transactions', TransactionViewSet, basename='transactions')

urlpatterns = router.urls