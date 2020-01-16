from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class LogInSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ()

    def create(self, validated_data):
        u_name = self.validated_data.POST.get('username')
        passw = self.validated_data.POST.get('password')
        user = authenticate(self.validated_data, username=u_name, password=passw)
        if user is not None:
            login(sel)
