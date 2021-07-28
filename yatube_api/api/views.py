# TODO:  Напишите свой вариант
from posts.models import Follow, Group, Post, User
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from .permissions import IsOwnerOrReadonly
from .serializers import PostSerializer,\
    CommentSerializer, GroupSerializer, FollowSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadonly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsOwnerOrReadonly]

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = get_object_or_404(
            User,
            username=self.request.user.username
        )
        return Follow.objects.filter(user=user).all()
