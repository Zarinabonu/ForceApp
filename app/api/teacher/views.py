from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView

from app.api.teacher.serializers import TeacherSerializer
from app.model import Teacher


class TeacherCreateAPIView(CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherUpdateAPIView(UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_url_kwarg = 'id'


class TeacherDestroyAPIView(DestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_url_kwarg = 'id'
