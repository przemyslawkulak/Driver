from rest_framework import serializers

from main.models import Tag, Advice, Training, Question, MyUser, Message


class TagSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='tagview',  # nazwa url-a szczegółów taga(name='tagview')
        lookup_field='pk'
    )

    class Meta:
        model = Tag
        fields = ('url', 'id', 'name',)  # bez dopisania url do listy, link pojawiłby się zamiast wartości id


class AdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advice
        fields = "__all__"


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
