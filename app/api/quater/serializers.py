from rest_framework.serializers import ModelSerializer

from app.model import Quater


class QuaterSerializer(ModelSerializer):
    class Meta:
        model = Quater
        fields = ('name',
                  'start_date',
                  'finish_date',
                  )