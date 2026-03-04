from rest_framework import serializers
from .models import Book
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'




class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'