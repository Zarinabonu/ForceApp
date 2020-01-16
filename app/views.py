from django.shortcuts import render
from django.views.generic import ListView

from app.model import Teacher, Class


class TeacherList(ListView):

    def get_context_data(self, *, object_list=None, **kwargs):
        teacher_all = Teacher.objects.all()
        c = Class.objects.all()
        for t in teacher_all:
            c = c.filter(teacher=t)

        context = {
            'teacher': teacher_all,
            'class': c,
        }

        return context





# Create your views here.
