from datetime import datetime

from django.db.models import Q
from rest_framework.generics import ListAPIView

from app.api.statistic.serializers import StatisticSerializer
from app.model import Subject, Student, ClassMember, Class


class StatisticListAPIView(ListAPIView):
    serializer_class = StatisticSerializer

    def get_queryset(self):
        qs = Subject.objects.all()
        today = datetime.today().date()
        print('student',today)

        stu = Student.objects.get(account__user=self.request.user)
        clas = Class.objects.get(classmember__student=stu)
        # qs = qs.filter(classsubject__class_id__classmember=member)
        qs = qs.filter(classsubject__class_id=clas).filter(classsubject__quater__start_date__lte=today).filter(classsubject__quater__finish_date__gte=today)
        print('qs',qs)

        return qs
