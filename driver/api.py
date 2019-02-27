from rest_framework import routers

from main.views import AdviceViewSet, TrainingViewSet, TagViewSet, QuestionViewSet, MessageViewSet, MyUserViewSet

router = routers.DefaultRouter()

router.register(r'advice', AdviceViewSet)
router.register(r'training', TrainingViewSet)
router.register(r'tag', TagViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'message', MessageViewSet)
router.register(r'myuser', MyUserViewSet)