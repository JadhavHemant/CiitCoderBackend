from rest_framework.views import APIView
from MyApp.models import *
from MyApp.Serializer import *
from rest_framework.response import Response
from rest_framework import status



class CityApi(APIView):
    def get(self, request,format=None):
        model=CitysModel.objects.all()
        serializer=CitysSerializer(model,many=True)
        return Response(serializer.data)

    def post(self,request,format=True):
        serializer=CitysSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class StateWiseCity(APIView):

    
class CityUpdateDeleteApi(APIView):
    def get_object(self,pk):
        try:
            return CitysModel.objects.get(pk=pk)
        except CitysModel.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND   
        
    def get(self, request, pk, format=None):
        city = self.get_object(pk)
        serializer = CitysSerializer(city)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        model = self.get_object(pk)
        serializer = CitysSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model = self.get_object(pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    