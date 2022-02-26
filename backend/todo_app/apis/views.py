from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from todos import models
from .serializers import TodoSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
  
class ClassBasedView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
  
    def get(self, request, format=None):
        content = {
            
            # `django.contrib.auth.User` instance
            'user': str(request.user),
            
            # None
            'auth': str(request.auth),
        }
        return Response(content)
    
class ListTodo(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer
    def get_queryset(self):
        return models.Todo.objects.filter(user=self.request.user)
    
class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer
    def get_queryset(self):
        return models.Todo.objects.filter(user=self.request.user)