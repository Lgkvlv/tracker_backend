from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication  # Добавляем импорт
from .models import Category, Transaction
from .serializers import CategorySerializer, TransactionSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]  # Добавляем аутентификацию
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        """Возвращаем только категории текущего пользователя"""
        return Category.objects.filter(user=self.request.user)

class TransactionViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]  # Добавляем аутентификацию
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TransactionSerializer
    
    def get_queryset(self):
        """Возвращаем только транзакции текущего пользователя"""
        return Transaction.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """Автоматически привязываем пользователя при создании"""
        serializer.save(user=self.request.user)
