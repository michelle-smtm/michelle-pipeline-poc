from .models import HelloWorld
from .serializers import HelloWorldSerializer
from rest_framework import generics
from django.http import JsonResponse

class HelloWorldListCreateAPIView(generics.ListCreateAPIView):
    queryset = HelloWorld.objects.all()
    serializer_class = HelloWorldSerializer

class HelloWorldDetailAPIView(generics.RetrieveAPIView):
    queryset = HelloWorld.objects.all()
    serializer_class = HelloWorldSerializer

class HelloWorldUpdatAPIView(generics.UpdateAPIView):
    queryset = HelloWorld.objects.all()
    serializer_class = HelloWorldSerializer

class HelloWorldDeleteAPIView(generics.DestroyAPIView):
    queryset = HelloWorld.objects.all()
    serializer_class = HelloWorldSerializer 

def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "Hello CD world!"})