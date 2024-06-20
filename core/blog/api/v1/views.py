from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .serialaizers import PostSerializer
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404



@api_view(["GET", "POST"])
def postList(request):
    if request.method == "GET":
       
        posts = Post.objects.all()
        serialaizers = PostSerializer(posts, many=True)
        return Response(serialaizers.data)
    elif request.method == "POST":
        serialaizers = PostSerializer(data=request.data)
        if serialaizers.is_valid():
            serialaizers.save()
            return Response(serialaizers.data, status=status.HTTP_201_CREATED)
        return Response(serialaizers.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET" , "PUT" , "DELETE"])
def postDetail(request , id):
   post = get_object_or_404(Post , pk=id , )
   if request.method == "GET":
       serialaizers = PostSerializer(post)
       return Response(serialaizers.data)
   elif request.method == "PUT":
       serialaizers = PostSerializer(post,data=request.data)
       if serialaizers.is_valid():
           serialaizers.save()
           return Response(serialaizers.data)
       return Response(serialaizers.errors, status=status.HTTP_400_BAD_REQUEST)
   elif request.method == 'DELETE':
       post.delete()
       return Response( {"details":"post was deleted"} , status=status.HTTP_204_NO_CONTENT)
   

#    try: 
#     post = Post.objects.get(pk=id)
#     serialaizers = PostSerializer(post)
#     return Response(serialaizers.data)
#    except Post.DoesNotExist:
#        return Response({"details":"post dose not exist"} , status=status.HTTP_404_NOT_FOUND)