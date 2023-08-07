from rest_framework.views import APIView
from MyApp.models import *
from MyApp.Serializer import *
from rest_framework.response import Response
from rest_framework import status



class CodeCommentReplayApis(APIView):
    def get(self, request,format=None):
        model=PostCommentReplys.objects.all()
        serializer=PostCommReplysSerializer(model,many=True)
        return Response(serializer.data)

    def post(self,request,format=True):
        serializer=PostCommReplysSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
class CodeCommentReplayApiUpdateDeleteApi(APIView):
    def get_object(self,pk):
        try:
            return PostCommentReplys.objects.get(pk=pk)
        except PostCommentReplys.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND   
        
    def get(self, request, pk, format=None):
        deltad = self.get_object(pk)
        serializer = PostCommReplysSerializer(deltad)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        model = self.get_object(pk)
        serializer = PostCommReplysSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model = self.get_object(pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    