from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

User = get_user_model()


class TelegramAuthView(APIView):
    def post(self, request):
        data = request.data
        telegram_user = data.get('user')

        if not telegram_user:
            return Response({'error': 'User data is required'}, status=400)

        user, created = User.objects.get_or_create(
            telegram_id=telegram_user.get('id'),
            defaults={
                'username': f"tg_{telegram_user.get('id')}",
                'first_name': telegram_user.get('first_name'),
                'last_name': telegram_user.get('last_name'),
            }
        )

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


from django.shortcuts import render

# Create your views here.
