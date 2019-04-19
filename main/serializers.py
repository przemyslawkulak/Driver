from rest_framework import serializers

from main.models import Tag, Advice, Training, Question, MyUser, Message


class TagSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='tagview',  # nazwa url-a szczegółów taga(name='tagview')
    #     lookup_field='pk'
    # )

    class Meta:
        model = Tag
        fields = ('url', 'id', 'name',)  # bez dopisania url do listy, link pojawiłby się zamiast wartości id


class AdviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advice
        fields = "__all__"


class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Training
        fields = "__all__"


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class MyUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ('url', 'id', 'username', 'email', 'last_login', 'date_joined', 'is_superuser', 'user_score')


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class AllQuestionSerializer(serializers.ModelField):
    child = TrainingSerializer(read_only=True)
    child_id = serializers.PrimaryKeyRelatedField(
        queryset=Training.objects.all(), source='training', write_only=True)

    class Meta:
        model = Question
        fields = "__al__"
