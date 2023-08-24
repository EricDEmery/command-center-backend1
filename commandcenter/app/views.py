from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import *
from .serializers import *
from django.db.models import Sum

class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
def UserSearch(request):
    username = request.GET.get('username')
    print(username)
    url = f"https://rocket-league1.p.rapidapi.com/ranks/{username}"  # Use the input username
    headers = {
        "User-Agent": "RapidAPI Playground",
        "Accept-Encoding": "identity",
        "X-RapidAPI-Key": "5fc0357622msh5ccf58c452c805dp156dafjsnf40ae832c05a",
        "X-RapidAPI-Host": "rocket-league1.p.rapidapi.com",
        "x-rapidapi-ua": "RapidAPI-Playground"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            return HttpResponse(json.dumps(user_data), status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Failed to fetch user data.'}, status=response.status_code)
        
    except requests.RequestException as e:
        return Response({'error': 'API request failed.', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)