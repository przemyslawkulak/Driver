# Create your views here.
from django.http import Http404
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, get_object_or_404

from main.models import Tag, Advice, Training, Question, Message, MyUser
from main.serializers import TagSerializer, AdviceSerializer, TrainingSerializer, MyUserSerializer, \
    MessageSerializer, QuestionSerializer


# 3(5) losowych porad +
# lista pytań na zasadzie porady (razem z poradą informacja czy wszystkie treningi do porady są zaliczone )
# pobierz trening do porady (wysyłanie pierwszego treningu w bazie)
# weryfikacja odpowiedzi (przesyłane, id pytania, odpowiedź -> zwracam 201/202) - weryfikować wszytkie odopwiedzi na raz
# wysłanie wiadmosci na forum (albo rekurencją albo Django MPTT)
# widok wysylający wszystkie porady związane z danym tagiem

# Token JWT -
# zapytania w curl - stworzenie nowej apki do sprawdzania zapytan API
# testy - warsztaty 6
# w readme - testy, aplikacja kliencka, endpointy,


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
#
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

# Django MPTT - klasa do budowania drzewa

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


###########################################################################################################
# MyUserViewSet

class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class RandomAdviceViewSet(viewsets.ModelViewSet):
    if len(Advice.objects.all()) > 3:
        queryset = Advice.objects.all().order_by('?')[:3]
    else:
        queryset = Advice.objects.all()
    serializer_class = AdviceSerializer


class AllQuestionsToAdviceView(ListAPIView):
    def get_queryset(self):
        try:
            advice = get_object_or_404(Advice, pk=self.kwargs['pk'])
            training = Training.objects.get(advice=advice)
            return Question.objects.filter(training=training)
        except Training.DoesNotExist:
            raise Http404

    permission_classes = []
    serializer_class = QuestionSerializer


# wyciągnąć jeden trening
class TrainingFromAdvice(ListAPIView):
    def get_queryset(self):
        advice = get_object_or_404(Advice, pk=self.kwargs['pk'])
        training = Training.objects.filter(advice=advice)
        return training

    serializer_class = TrainingSerializer

# class AllQuestionsToAdviceView(APIView):
#
#     def get_object(self, pk=1):
#         try:
#             return Training.objects.get(pk=pk)
#         except Training.DoesNotExist:
#             raise Http404
#
#
#     def get(self, request, format=None, pk=1):
#         # training = Training.objects.get(advice=self.get_object(pk))
#         queryset = Question.objects.filter(training=self.get_object(pk))
#         serializer = AllQuestionSerializer(queryset, context={"request": request})
#         return Response(serializer.data)

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
