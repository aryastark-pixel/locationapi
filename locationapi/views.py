from django.shortcuts import render
from rest_framework.views import APIView, status
from locationApp.models import BeatPersonnelOne
from locationapi.serializers import BeatPersonnelSerializer

from rest_framework.response import Response
class GetLocationApi(APIView):

    def get (self, request,pk=None,format= None):
         id=pk
         if id is not None:
              location= BeatPersonnelOne.objects.get(id=id)
              serializer = BeatPersonnelSerializer(location)
              return Response(serializer.data)
         location = BeatPersonnelOne.objects.all()
         serializer = BeatPersonnelSerializer(location, many= True)
         return Response(serializer.data,status=status.HTTP_200_OK )

class PostLocationApi(APIView):
    def post(self, request, format=None):
        serializer = BeatPersonnelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
