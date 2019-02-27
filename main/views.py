from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Tag
from main.serializers import TagSerializer


####################################################################################################
# TagView


class TagList(APIView):

    def get(self, request, format=None):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagView(APIView):

    def get_object(self, id):
        try:
            return Tag.objects.get(id=id)
        except Tag.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        tag = self.get_object(id)
        serializer = TagSerializer(tag, context={"request": request})
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        tag = self.get_object(id)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id, format=None):
        tag = self.get_object(id)
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id, format=None):
        pass

###########################################################################################################
# AdviceView
