from rest_framework.generics import CreateAPIView, DestroyAPIView

from app.api.subject.serializers import SubjectSerializer
from app.model import Subject


class SubjectCreateAPIView(CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDestroyAPIView(DestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    lookup_url_kwarg = 'id'