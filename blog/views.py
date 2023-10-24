from http.client import HTTPResponse

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Post
from blog.serializers import PostSerializer


# Create your views here.
@api_view(["GET"])
def index(request):
    return Response(
        {
            "data": [
                {"name": "Lei Song",
                 "address": "123 Carrington Road",
                 "phone": "1233242"
                 },
                {"name": "Chris",
                 "address": "123 Carrington Road",
                 "phone": "1233242"
                 },
            ]
        }
    )


@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

