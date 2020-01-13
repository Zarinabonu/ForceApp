from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes

from app.model import Parent, Account


class ParentSerializer(ModelSerializer):
    f_name = serializers.CharField(max_length=100, write_only=True)
    l_name = serializers.CharField(max_length=100, write_only=True)
    m_name = serializers.CharField(max_length=100, write_only=True)
    phone = serializers.IntegerField(write_only=True)
    photo = serializers.ImageField(write_only=True)
    address = serializers.CharField(max_length=200, write_only=True)

    class Meta:
        model = Parent
        fields = ('f_name',
                  'l_name',
                  'm_name',
                  'phone',
                  'photo',
                  'address',)

    def create(self, validated_data):
        first_name = validated_data.pop('f_name')
        last_name = validated_data.pop('l_name')
        middle_name = validated_data.pop('m_name')
        phone = validated_data.pop('phone')
        photo = validated_data.pop('photo')
        address = validated_data.pop('address')

        p = Parent(**validated_data)
        a = Account.objects.create(f_name=first_name, l_name=last_name, m_name=middle_name, phone=phone, photo=photo, address=address)
        a.save()
        p.account = a
        p.save()
        print(p)
        return p

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        if validated_data.get('password'):
            p = validated_data.pop('password')
            instance.account.user.set_password(p)
        for attr, value in validated_data.items():
            setattr(instance.account, attr, value)
            setattr(instance, attr, value)

        instance.account.save()
        instance.save()

        return instance
