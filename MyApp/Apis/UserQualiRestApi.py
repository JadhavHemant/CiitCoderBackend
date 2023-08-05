from rest_framework.views import APIView
from MyApp.models import *
from MyApp.Serializer import *
from rest_framework.response import Response
from rest_framework import status

class UserQualiApi(APIView):
    def get(self, request,format=None):
        model=QualiModel.objects.all()
        serializer=QualiSerializer(model,many=True)
        return Response(serializer.data)

    def post(self,request,format=True):
        serializer=QualiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    
class UserQualiUpdateDeleteApi(APIView):
    def get_object(self,pk):
        try:
            return QualiModel.objects.get(pk=pk)
        except QualiModel.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND   
        
    def get(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = QualiSerializer(location)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        model = self.get_object(pk)
        serializer = QualiSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model = self.get_object(pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    