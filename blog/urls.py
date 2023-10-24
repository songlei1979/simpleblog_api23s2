from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.views import index, post_list
from blog.viewsets import PostViewSet

router = DefaultRouter()
router.register("posts", PostViewSet, "posts")

urlpatterns = [
    path("", index, name="Home"),
    path("list_posts/", post_list, name="post_list"),
    path("api/", include(router.urls))
]