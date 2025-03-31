from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer, Transaction
import json

@api_view(['GET'])
def get_balance(request):
    user_id = request.GET.get('user_id')
    customer, _ = Customer.objects.get_or_create(user_id=user_id)
    return Response({'balance': customer.balance})

@api_view(['POST'])
def add_points(request):
    try:
        data = json.loads(request.body)
        customer = Customer.objects.get(user_id=data['user_id'])
        Transaction.objects.create(
            customer=customer,
            points=data['points'],
            description=data.get('description', 'Начисление')
        )
        customer.balance += data['points']
        customer.save()
        return Response({'status': 'ok'})
    except Exception as e:
        return Response({'error': str(e)}, status=400)