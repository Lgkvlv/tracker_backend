from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transaction, Category

@api_view(['GET'])
def transaction_list(request):
    user_id = request.GET.get('user_id')
    transactions = Transaction.objects.filter(user_id=user_id).order_by('-date')
    data = [
        {
            "id": t.id,
            "amount": str(t.amount),
            "category": t.category,
            "date": t.date.isoformat()
        }
        for t in transactions
    ]
    return Response(data)

@api_view(['GET'])
def category_list(request):
    user_id = request.GET.get('user_id')
    categories = Category.objects.filter(user_id=user_id)
    data = [{"id": c.id, "name": c.name} for c in categories]
    return Response(data)

@api_view(['POST'])
def add_transaction(request):
    user_id = request.data.get('user_id')
    amount = request.data.get('amount')
    category = request.data.get('category')
    
    Transaction.objects.create(
        user_id=user_id,
        amount=amount,
        category=category
    )
    return Response({"status": "ok"})
