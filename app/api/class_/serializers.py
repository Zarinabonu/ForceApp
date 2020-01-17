from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes

from app.api.quater.serializers import QuaterSerializer
from app.api.subject.serializers import SubjectSerializer
from app.api.teacher.serializers import TeacherSerializer
from app.model import Class, Teacher, ClassSubject, Subject, Quater, ClassMember, Student


class ClassSerializer(ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    teacher_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Class
        fields = ('teacher',
                  'teacher_id',
                  'name',)

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        if validated_data.get('teacher_id'):
            p = validated_data.pop('teacher_id')
            print(instance.teacher)
            t = Teacher.objects.get(id=p)
            instance.teacher = t
            instance.teacher.save()
            print(instance.teacher)
        c_name = validated_data.get('name')
        instance.name = c_name
        print(instance.teacher)

        instance.save()

        return instance


class ClassSubjectSerializer(ModelSerializer):
    class_id = ClassSerializer(read_only=True)
    class_id_id = serializers.IntegerField(write_only=True)
    subject = SubjectSerializer(read_only=True)
    subject_id = serializers.IntegerField(write_only=True)
    teacher = TeacherSerializer(read_only=True)
    teacher_id = serializers.IntegerField(write_only=True)
    quater = QuaterSerializer(read_only=True)
    quater_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ClassSubject
        fields = ('class_id',
                  'class_id_id',
                  'subject',
                  'subject_id',
                  'teacher',
                  'teacher_id',
                  'quater',
                  'quater_id',
                  'start_date',
                  'finish_date',
                  'day')

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        if validated_data.get('class_id_id'):
            c = validated_data.pop('class_id_id')
            cla = Class.objects.get(id=c)
            print(c)
            instance.class_id = cla
            instance.class_id.save()
        if validated_data.get('subject_id'):
            s = validated_data.pop('subject_id')
            sub = Subject.objects.get(id=s)
            instance.subject = sub
            instance.subject.save()
        if validated_data.get('teacher_id'):
            t = validated_data.pop('teacher_id')
            teach = Teacher.objects.get(id=t)
            instance.teacher = teach
            instance.teacher.save()
        if validated_data.get('quater_id'):
            q = validated_data.pop('quater_id')
            qua = Quater.objects.get(id=q)
            instance.quater = qua
            instance.quater.save()
        start_d = validated_data.get('start_date')
        instance.start_date = start_d
        finish_d = validated_data.get('finish_date')
        instance.finish_date = finish_d
        d = validated_data.get('day')
        instance.day = d

        instance.save()
        return instance


class ClassMemberSerializer(ModelSerializer):
    class_id = ClassSerializer(read_only=True)
    class_id_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ClassMember
        fields = ('class_id',
                  'class_id_id',)

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        if validated_data.get('class_id_id'):
            p = validated_data.pop('class_id_id')
            t = Class.objects.get(id=p)
            instance.class_id = t
            instance.class_id.save()


        instance.save()

        return instance


class ClassListSerializer(ModelSerializer):
    class Meta:
        model = Class
        fields = ('id',
                  'name')

