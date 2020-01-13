from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView

from app.api.parent.serializers import ParentSerializer
from app.model import Parent


class ParentCreateAPIView(CreateAPIView):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()


class ParentUpdateAPIView(UpdateAPIView):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()
    lookup_url_kwarg = 'id'

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class ParentDestroyAPIView(DestroyAPIView):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()
    lookup_url_kwarg = 'id'


