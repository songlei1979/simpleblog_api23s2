from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from blog.models import Post
from blog.permissions import IsAuthorOrReadOnly
from blog.serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, )

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )