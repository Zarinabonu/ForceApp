from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView

from app.api.class_.serializers import ClassSerializer, ClassSubjectSerializer
from app.model import Class, ClassSubject


class ClassCreateAPIView(CreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassUpdateAPIView(UpdateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    lookup_url_kwarg = 'id'


class ClassDestroyAPIView(DestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    lookup_url_kwarg = 'id'


class ClassSubjectCreateAPIView(CreateAPIView):
    queryset = ClassSubject.objects.all()
    serializer_class = ClassSubjectSerializer


class ClassSubjectUpdateAPIView(UpdateAPIView):
    queryset = ClassSubject.objects.all()
    serializer_class = ClassSubjectSerializer
    lookup_url_kwarg = 'id'


class ClassSubjectDestroyAPIView(DestroyAPIView):
    queryset = ClassSubject.objects.all()
    serializer_class = ClassSubjectSerializer
    lookup_url_kwarg = 'id'