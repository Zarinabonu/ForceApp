from rest_framework.serializers import ModelSerializer

from app.model import Account


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ('id',
                  'f_name',
                  'l_name',
                  'm_name',)
