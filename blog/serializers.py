from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField(method_name="get_author_name")
    class Meta:
        model = Post
        fields = ["id", "title", "body","author","author_name"]

    @staticmethod
    def get_author_name(instance):
        author_name = instance.author.first_name + " " + instance.author.last_name
        return author_name



