from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.api.homework.serializers import HomeworkListSerializer
from app.model import Subject, Homework


class SubjectSerializer(ModelSerializer):
    own_homework = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        fields = ('id',
                  'name',
                  'own_homework')

    def get_own_homework(self, obj):
        qs = Homework.objects.filter(subject=obj)
        return HomeworkListSerializer(qs, many=True, context=self.context).data


class SubjectListSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id',
                  'name')