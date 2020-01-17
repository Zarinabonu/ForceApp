from rest_framework.generics import ListAPIView

from app.api.news.serializers import NewsSerializer
from app.model import News


class NewsListAPIView(ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        qs = News.objects.all()
        v = self.request.GET.get('-views')
        l_seen = self.request.GET.get('last_seen')
        if v:
            qs = qs.order_by('views')
        if l_seen:
            qs = qs.order_by('-created')
        return qs


