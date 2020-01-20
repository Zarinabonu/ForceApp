from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView

from app.api.teacher.serializers import TeacherSerializer, TeacherCSerializer
from app.model import Teacher


class TeacherCreateAPIView(CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCSerializer


class TeacherUpdateAPIView(UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCSerializer
    lookup_url_kwarg = 'id'


class TeacherDestroyAPIView(DestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCSerializer
    lookup_url_kwarg = 'id'
