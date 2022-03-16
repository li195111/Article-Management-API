# article_manage/views.py

from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework import permissions

from .models import Article, Author
from .serializers import UserSerializer, GroupSerializer, ArticleSerializer, AuthorSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [ permissions.IsAuthenticated ]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [ permissions.IsAuthenticated ]

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Author to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [ permissions.IsAuthenticated, ]

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ArticleViewSet to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [ permissions.IsAuthenticated, ]
    