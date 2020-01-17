from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes

from app.api.account.serializers import AccountSerializer
from app.api.subject.serializers import SubjectListSerializer
from app.model import Teacher, Account, Subject


class TeacherSerializer(ModelSerializer):
    f_name = serializers.CharField(max_length=100, write_only=True)
    l_name = serializers.CharField(max_length=100, write_only=True)
    m_name = serializers.CharField(max_length=100, write_only=True)
    photo = serializers.ImageField(write_only=True)
    phone = serializers.IntegerField(write_only=True)
    address = serializers.CharField(max_length=200, write_only=True)

    class Meta:
        model = Teacher
        fields = ('f_name',
                  'l_name',
                  'm_name',
                  'photo',
                  'phone',
                  'address',
                  )

    def create(self, validated_data):
        first_name = validated_data.pop('f_name')
        last_name = validated_data.pop('l_name')
        middle_name = validated_data.pop('m_name')
        photo = validated_data.pop('photo')
        phone = validated_data.pop('phone')
        address = validated_data.pop('address')

        t = Teacher(**validated_data)
        a = Account.objects.create(f_name=first_name, l_name=last_name, m_name=middle_name, photo=photo, phone=phone, address=address)
        t.account = a
        t.save()
        return t

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


class TeacherSerializer(ModelSerializer):
    account = AccountSerializer(read_only=True)
    subject_set = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ('id',
                  'account',
                  'subject_set')

    def get_subject_set(self, obj):
        qs = Subject.objects.filter(classsubject__teacher=obj)
        return SubjectListSerializer(qs, many=True, context=self.context).data