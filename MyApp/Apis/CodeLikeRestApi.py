from rest_framework.views import APIView
from MyApp.models import *
from MyApp.Serializer import *
from rest_framework.response import Response
from rest_framework import status



class CodeLikeApis(APIView):
    def get(self, request,format=None):
        model=PostLikesDislikesTBModel.objects.all()
        serializer=PostLikesDislikesSerializer(model,many=True)
        return Response(serializer.data)

    def post(self,request,format=True):
        serializer=PostLikesDislikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
class CodeLikeApiUpdateDeleteApi(APIView):
    def get_object(self,pk):
        try:
            return PostLikesDislikesTBModel.objects.get(pk=pk)
        except PostLikesDislikesTBModel.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND   
        
    def get(self, request, pk, format=None):
        deltad = self.get_object(pk)
        serializer = PostLikesDislikesSerializer(deltad)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        model = self.get_object(pk)
        serializer = PostLikesDislikesSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model = self.get_object(pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    