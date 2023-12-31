from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Post, Category, Comment, Profile


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField(method_name="get_author_name")
    class Meta:
        model = Post
        fields = ["id", "title", "body","author","author_name"]

    @staticmethod
    def get_author_name(instance):
        author_name = instance.author.first_name + " " + instance.author.last_name
        return author_name

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "first_name"]

        extra_kwargs = {
            "password":{
                "write_only":True,
                "required":True
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "comment", "post", "user"]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "address", "phone_number", "user", "web_page"]


