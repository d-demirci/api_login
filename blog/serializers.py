from rest_framework import  serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Post, Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','url', 'username', 'email', 'first_name', 'last_name', 'is_staff']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['url','title','user', 'content']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [ 'content', 'user']


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ('key', 'user')