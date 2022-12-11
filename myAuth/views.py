from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import CustomUser
from .serializers import MyAuthSerializer, RegisterSerializer


@api_view(['POST', ])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['response'] = "successfully registered a new user."
        data['phone'] = str(user.phone_number)
        data['email'] = user.email
    else:
        data = serializer.errors
    return Response(data)


@api_view(['GET', 'POST'])
def get_user(request, *args, **kwargs):
    instance = CustomUser.objects.all()
    data = {}
    if instance:
        data = MyAuthSerializer(instance).data
    return Response(data)
