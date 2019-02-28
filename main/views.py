from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Tag, Advice, Training, Question, Message, MyUser
from main.serializers import TagSerializer, AdviceSerializer, TrainingSerializer, QuestionSerializer, MessageSerializer, \
    MyUserSerializer


####################################################################################################
# TagView


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

# class TagList(APIView):
#
#     def get(self, request, format=None):
#         tags = Tag.objects.all()
#         serializer = TagSerializer(tags, many=True, context={"request": request})
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = TagSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class TagView(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Tag.objects.get(pk=pk)
#         except Tag.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         tag = self.get_object(pk)
#         serializer = TagSerializer(tag, context={"request": request})
#         return Response(serializer.data)
#
#     def delete(self, request, pk, format=None):
#         tag = self.get_object(pk)
#         tag.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def put(self, request, pk, format=None):
#         tag = self.get_object(pk)
#         serializer = TagSerializer(tag, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def post(self, request, pk, format=None):
#         pass


###########################################################################################################
# AdviceView

class AdviceViewSet(viewsets.ModelViewSet):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer


###########################################################################################################
# TrainingView

class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

###########################################################################################################
# QuestionViewSet

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

###########################################################################################################
# MessageViewSet

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


###########################################################################################################
# MyUserViewSet

class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer