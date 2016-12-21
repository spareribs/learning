from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import PoemSerializer
from .models import Poem
from rest_framework.decorators import api_view
# Create your views here.


class PoemListView(APIView):
    def get(self, request, format=None):
        poems = Poem.objects.all()
        serializer = PoemSerializer(poems, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PoemSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def poem_detail(request, pk):
    try:
        poem = Poem.objects.get(pk=pk)
    except Poem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PoemSerializer(poem)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PoemSerializer(Poem, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        poem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
