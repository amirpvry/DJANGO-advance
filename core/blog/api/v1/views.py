from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serialaizers import PostSerializer , CategorySerializer
from blog.models import Post , Categories
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets



# @api_view(["GET", "POST"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def postList(request):
#     if request.method == "GET":
       
#         posts = Post.objects.filter(status = True)
#         serialaizers = PostSerializer(posts, many=True)
#         return Response(serialaizers.data)
#     elif request.method == "POST":
#         serialaizers = PostSerializer(data=request.data)
#         serialaizers.is_valid(raise_exception= True)
#         serialaizers.save()
#         return Response(serialaizers.data,)

    

# class PostList(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer

#     def get(self, request):
#         posts = Post.objects.filter(status = True)
#         serialaizers = PostSerializer(posts, many=True)
#         return Response(serialaizers.data)
#     def post(self, request):
#         serialaizers = PostSerializer(data=request.data)
#         serialaizers.is_valid(raise_exception= True)
#         serialaizers.save()
#         return Response(serialaizers.data,)
    

class PostViewSetModel(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

class CategorySetModel(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Categories.objects.all()





# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = v
#     queryset = Post.objects.filter(status=True)
    




    
        
# @api_view(["GET" , "PUT" , "DELETE"])
# @permission_classes([IsAuthenticated])
# def postDetail(request , id):
#    post = get_object_or_404(Post , pk=id ,status= True )
#    if request.method == "GET":
#        serialaizers = PostSerializer(post)
#        return Response(serialaizers.data)
#    elif request.method == "PUT":
#        serialaizers = PostSerializer(post,data=request.data)
#        if serialaizers.is_valid():
#            serialaizers.save()
#            return Response(serialaizers.data)
#        return Response(serialaizers.errors, status=status.HTTP_400_BAD_REQUEST)
#    elif request.method == 'DELETE':
#        post.delete()
#        return Response( {"details":"post was deleted"} , status=status.HTTP_204_NO_CONTENT)
   
# class PostDetail(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     def get(self, request, id):
#         post = get_object_or_404(Post, pk=id, status=True)
#         serialaizers = PostSerializer(post)
#         return Response(serialaizers.data)
#     def put(self, request, id):
#         post = get_object_or_404(Post, pk=id, status=True)
#         serialaizers = PostSerializer(post, data=request.data)
#         serialaizers.is_valid(raise_exception= True)
#         serialaizers.save()
#         return Response(serialaizers.data)
    
#     def delete(self, request, id):
#         post = get_object_or_404(Post, pk=id, status=True)
#         post.delete()
#         return Response({"details":"post was deleted"} , status=status.HTTP_204_NO_CONTENT)
   

#    try: 
#     post = Post.objects.get(pk=id)
#     serialaizers = PostSerializer(post)
#     return Response(serialaizers.data)
#    except Post.DoesNotExist:
#        return Response({"details":"post dose not exist"} , status=status.HTTP_404_NOT_FOUND)