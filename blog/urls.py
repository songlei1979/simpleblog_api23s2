from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.views import index, post_list, get_user_id
from blog.viewsets import PostViewSet, UserViewSet

router = DefaultRouter()
router.register("posts", PostViewSet, "posts")
router.register("users", UserViewSet, "users")

urlpatterns = [
    path("", index, name="Home"),
    path("list_posts/", post_list, name="post_list"),
    path("api/", include(router.urls)),
    path("get_user_id/", get_user_id, name="get_user_id")
]