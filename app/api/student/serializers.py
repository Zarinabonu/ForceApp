from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes

from app.api.account.urls import AccountSerializer
from app.api.attandance.serializers import AttandanceListSerializer
from app.api.class_.serializers import ClassListSerializer
from app.api.homework.serializers import HomeworkListSerializer
from app.api.mark.serializers import MarkListSerializer
from app.api.notification.serializers import NotificationListSerializer
from app.api.school.serializers import SchoolListSerializer
from app.api.subject.serializers import SubjectSerializer
from app.api.teacher.serializers import TeacherSerializer
from app.model import Student, Account, Class, Attandance, Marks, Homework, Subject, ClassSubject, Teacher, Notification
from app.model.school import School


class StudentSerializer(ModelSerializer):
    f_name = serializers.CharField(max_length=100, write_only=True)
    l_name = serializers.CharField(max_length=100, write_only=True)
    m_name = serializers.CharField(max_length=100, write_only=True)
    phone = serializers.IntegerField(write_only=True)
    photo = serializers.ImageField(write_only=True)
    address = serializers.CharField(max_length=200, write_only=True)

    class Meta:
        model = Student
        fields = ('f_name',
                  'l_name',
                  'm_name',
                  'phone',
                  'photo',
                  'address',
                  )

    def create(self, validated_data):
        first_name = validated_data.pop('f_name')
        last_name = validated_data.pop('l_name')
        middle_name = validated_data.pop('m_name')
        phone = validated_data.pop('phone')
        photo = validated_data.pop('photo')
        address = validated_data.pop('address')

        s = Student(**validated_data)
        a = Account.objects.create(f_name=first_name, l_name=last_name, m_name=middle_name, phone=phone, photo=photo, address=address)
        s.account = a
        s.save()
        return s

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


class StudentListSerializer(ModelSerializer):
    account = AccountSerializer(read_only=True)
    own_class = serializers.SerializerMethodField()
    own_school = serializers.SerializerMethodField()
    attandance_set = serializers.SerializerMethodField()
    mark_set = serializers.SerializerMethodField()
    subject_set = serializers.SerializerMethodField()
    teacher_set = serializers.SerializerMethodField()
    notification_set = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ('id',
                  'account',
                  'own_class',
                  'own_school',
                  'attandance_set',
                  'mark_set',
                  'subject_set',
                  'teacher_set',
                  'notification_set')

    def get_own_class(self, obj):
        qs = Class.objects.filter(classmember__student=obj)
        return ClassListSerializer(qs, many=True, context=self.context).data

    def get_own_school(self, obj):
        qs = School.objects.filter(student=obj)
        return SchoolListSerializer(qs, many=True, context=self.context).data

    def get_attandance_set(self, obj):
        qs = Attandance.objects.filter(student=obj)
        return AttandanceListSerializer(qs, many=True, context=self.context).data

    def get_mark_set(self, obj):
        qs = Marks.objects.filter(class_member__student=obj)
        return MarkListSerializer(qs, many=True, context=self.context).data

    def get_subject_set(self, obj):
        c = Class.objects.get(classmember__student=obj)
        qs = Homework.objects.filter(class_subject__class_id=c)
        return HomeworkListSerializer(qs, many=True, context=self.context).data

    def get_teacher_set(self, obj):
        qs = Teacher.objects.filter(account__student=obj)
        return TeacherSerializer(qs, many=True, context=self.context).data

    def get_notification_set(self, obj):
        qs = Notification.objects.all().order_by('-created')
        return NotificationListSerializer(qs, many=True, context=self.context).data




