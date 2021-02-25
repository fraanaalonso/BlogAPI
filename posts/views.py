from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer