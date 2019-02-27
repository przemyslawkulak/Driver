from django.contrib import admin

# Register your models here.
from main.models import MyUser, Tag, Training, Question, Message, Advice

admin.site.register(MyUser)
admin.site.register(Tag)
admin.site.register(Advice)
admin.site.register(Training)
admin.site.register(Question)
admin.site.register(Message)
