from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import json

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
