# article_manage/serializers.py

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Author, Article

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']
        
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'tags', 'content', 'create_at', 'update_at', 'author']