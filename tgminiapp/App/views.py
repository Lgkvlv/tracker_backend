from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Transaction, Category
import json

# GET /api/transactions – список транзакций
@csrf_exempt  # Отключаем CSRF для API (для теста)
def transaction_list(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')  # Получаем user_id из запроса
        transactions = Transaction.objects.filter(user_id=user_id).values()
        return JsonResponse(list(transactions), safe=False)
    return JsonResponse({'error': 'Only GET allowed'}, status=405)

# GET /api/categories – список категорий
@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        categories = Category.objects.filter(user_id=user_id).values()
        return JsonResponse(list(categories), safe=False)
    return JsonResponse({'error': 'Only GET allowed'}, status=405)

# POST /api/add_transaction – добавление транзакции
@csrf_exempt
def add_transaction(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Читаем JSON из тела запроса
            Transaction.objects.create(
                user_id=data['user_id'],
                amount=data['amount'],
                category=data['category']
            )
            return JsonResponse({'status': 'ok'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Only POST allowed'}, status=405)
    
