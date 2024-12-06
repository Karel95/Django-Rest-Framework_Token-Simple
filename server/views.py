from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer


@api_view(['POST'])
def register(request):
  # Validate and save the user data using the UserSerializer from serializers.py.
  serializer = UserSerializer(data = request.data)
  
  if serializer.is_valid():
    serializer.save()
    user = User.objects.get(username = serializer.data['username'])
    user.set_password(serializer.data['password'])
    user.save()
    
    token = Token.objects.create(user=user)
    return Response({'token': token.key, 'user': serializer.data}, status = status.HTTP_201_CREATED)
  
  return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
  return Response({})

@api_view(['POST'])
def profile(request):
  return Response({})


# @api_view(['POST'])
# def update_profile(request):
#   return Response({})

# @api_view(['POST'])
# def upload_photo(request):
#   return Response({})

# @api_view(['POST'])
# def change_password(request):
#   return Response({})

# @api_view(['POST'])
# def forgot_password(request):
#   return Response({})