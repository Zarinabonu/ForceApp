from rest_framework.serializers import ModelSerializer

from app.model import News


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ('id',
                  'title',
                  'image',
                  'short_content',
                  'created')