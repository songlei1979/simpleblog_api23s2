from django.urls import path

from blog.views import index, post_list

urlpatterns = [
    path("", index, name="Home"),
    path("list_posts/", post_list, name="post_list"),
]