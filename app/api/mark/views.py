from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView

from app.api.mark.serializers import MarkSerializer
from app.model import Marks


class MarkCreateAPIView(CreateAPIView):
    queryset = Marks.objects.all()
    serializer_class = MarkSerializer


class MarkUpdateAPIView(UpdateAPIView):
    queryset = Marks.objects.all()
    serializer_class = MarkSerializer
    lookup_url_kwarg = 'id'


class MarkDestroyAPIView(DestroyAPIView):
    queryset = Marks.objects.all()
    serializer_class = MarkSerializer
    lookup_url_kwarg = 'id'