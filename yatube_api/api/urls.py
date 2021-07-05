from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments')
router_v1.register(r'group',
                   GroupViewSet, basename='group')
router_v1.register(r'follow',
                   FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router_v1.urls)),
]
