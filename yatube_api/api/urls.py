from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import CommentsViewSet, GroupsViewSet, PostsViewsSet

v1_router = routers.DefaultRouter()
v1_router.register(r'v1/posts', PostsViewsSet)
v1_router.register(r'v1/groups', GroupsViewSet)
v1_router.register(
    r'^v1/posts/(?P<post_id>\d+)/comments',
    CommentsViewSet,
    basename='comments'
)


urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('', include(v1_router.urls)),
]
