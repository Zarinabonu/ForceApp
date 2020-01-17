from rest_framework.serializers import ModelSerializer

from app.model import Notification


class NotificationListSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id',
                  'notification',
                  'date')