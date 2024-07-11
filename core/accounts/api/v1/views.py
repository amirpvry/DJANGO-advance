from rest_framework import viewsets , generics

from rest_framework.response import Response

from .serialaizers import RecursionSerializer
from rest_framework import status

class RegesterationApiView(generics.GenericAPIView):
   
    serializer_class = RecursionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'email': serializer.validated_data['email']
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


