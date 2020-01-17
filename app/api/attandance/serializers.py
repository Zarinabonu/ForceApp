from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.api.subject.serializers import SubjectListSerializer
from app.model import Attandance, Subject


class AttandanceListSerializer(ModelSerializer):
    own_subject = serializers.SerializerMethodField()

    class Meta:
        model = Attandance
        fields = ('id',
                  'attandance',
                  'own_subject')

    def get_own_subject(self, obj):
        qs = Subject.objects.filter(classsubject__attandance=obj)
        return SubjectListSerializer(qs, many=True, context=self.context).data