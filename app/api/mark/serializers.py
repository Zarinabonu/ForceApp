from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes

from app.api.class_.serializers import ClassMemberSerializer, ClassSubjectSerializer
from app.api.subject.serializers import SubjectListSerializer
from app.model import Marks, ClassMember, ClassSubject, Subject


class MarkSerializer(ModelSerializer):
    class_member = ClassMemberSerializer(read_only=True)
    class_member_id = serializers.IntegerField(write_only=True)
    class_subject_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Marks
        fields = ('class_member',
                  'class_member_id',
                  'class_subject_id',
                  'mark',
                  'is_finil')

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        if validated_data.get('class_member_id'):
            p = validated_data.pop('class_member_id')
            t = ClassMember.objects.get(id=p)
            instance.class_member = t
            instance.class_member.save()
        if validated_data.get('class_subject_id'):
            p = validated_data.pop('class_subject_id')
            s = Subject.objects.get(id=p)
            instance.class_subject = s
            instance.class_subject.save()
        m = validated_data.get('mark')
        instance.mark = m
        instance.save()

        return instance


class MarkListSerializer(ModelSerializer):
    class_subject = SubjectListSerializer(read_only=True)

    class Meta:
        model = Marks
        fields = ('id',
                  'class_subject',
                  'mark',
                  'is_finil')