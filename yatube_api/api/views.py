from rest_framework import filters, viewsets, serializers, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.shortcuts import get_object_or_404

from .models import Comment, Follow, Group, Post, User
from .permissions import IsAuthorPermission
from .serializers import CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer

PERMISSION_CLASSES = (IsAuthenticatedOrReadOnly, IsAuthorPermission,)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = PERMISSION_CLASSES

    def get_queryset(self):
        queryset = Post.objects.all()
        group = self.request.query_params.get('group', None)
        if group is not None:
            queryset = queryset.filter(group=group)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = PERMISSION_CLASSES

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = PERMISSION_CLASSES

    def perform_create(self, serializer):
        serializer.save()


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['following__username', 'user__username', ]

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.request.user.pk)
        queryset = user.following.all()
        return queryset

    def perform_create(self, serializer):
        print(f'hehe {self.request.user}')
        serializer.save(user=self.request.user)

