from rest_framework import serializers
from blog.models import Post , Categories

# class PostSerializer(serializers.Serializer):

#     id = serializers.IntegerField(required=True)
#     title = serializers.CharField(max_length=200)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['name']


class PostSerializer(serializers.ModelSerializer):

    related_url = serializers.URLField(source='get_absolute_api_url' , read_only=True)
    absolute_api_url = serializers.SerializerMethodField(method_name='get_abs_api_url')
    
    

    class Meta:

        model = Post
        fields = ['id','author', 'title', 'content', 'categories' , 'status' , 'related_url' , 'absolute_api_url']
        read_only_fields = ['content']

    def get_abs_api_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['categories'] = CategorySerializer(instance.categories).data
        rep.pop('related_url')
        return rep
    

 