from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer

class UserProfile(APIView): #Информация о профиле пользователя. Требуется войти в систему

    def get(self, request):
        user = request.user
        try:
            data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            }
        except AttributeError:
            return Response(status=401)
        return Response(data=data)

class CreateUserView(APIView): #Регистрация нового пользователя
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(status=400)