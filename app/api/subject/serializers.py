from rest_framework.serializers import ModelSerializer

from app.model import Subject


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name',
                  )