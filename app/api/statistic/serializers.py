from django.db.models import Avg
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from app.api.mark.serializers import MarkSerializer
from app.model import Subject, Marks


class StatisticSerializer(ModelSerializer):
    mark_set = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        fields = ('id',
                  'name',
                  'mark_set')

    def get_mark_set(self, obj):
        qs = Marks.objects.filter(class_subject__subject=obj).aggregate(Avg('mark'))
        return qs
    #     qs = Marks.objects.filter(class_member__marks__class_subject=obj).aggregate(Avg('mark'))
    #     return qs