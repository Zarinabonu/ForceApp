from rest_framework.serializers import ModelSerializer

from app.model import Homework


class HomeworkListSerializer(ModelSerializer):
    class Meta:
        model = Homework
        fields = ('id',
                  'name')