from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serialaizers import PostSerializer , CategorySerializer
from blog.models import Post , Categories
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters





class PostViewSetModel(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly , IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend , filters.SearchFilter]
    filterset_fields = ['status' , 'categories' , 'content' ]
    search_fields = ['title']

class CategorySetModel(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Categories.objects.all()





