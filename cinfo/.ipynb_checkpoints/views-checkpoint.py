from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import *
from .serializers import *

# Create your views here.

class getActors(APIView):

    def get(self,request):
        actrs = Actors.objects.all()
        print(actrs)
        serializer = actorSerializer(actrs, many=True)
        print('ser',serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = actorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        item = Actors.objects.get(pk=pk)
        data = actorSerializer(instance=item, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        item = Actors.objects.filter(id=pk)
        print(item)
        item.delete()
        print(f'deleted {item}')
        return Response(status=status.HTTP_202_ACCEPTED)