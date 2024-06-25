from rest_framework import serializers
from blog.models import Post

# class PostSerializer(serializers.Serializer):

#     id = serializers.IntegerField(required=True)
#     title = serializers.CharField(max_length=200)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'categories' , 'status']


 