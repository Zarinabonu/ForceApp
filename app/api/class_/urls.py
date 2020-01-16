from django.urls import path

from app.api.class_ import views

urlpatterns = [
    path('create', views.ClassCreateAPIView.as_view(), name='api-class-create'),
    path('update/<int:id>', views.ClassUpdateAPIView.as_view(), name='api-class-update'),
    path('destroy/<int:id>', views.ClassDestroyAPIView.as_view(), name='api-class-destroy'),
    path('subject/create', views.ClassSubjectCreateAPIView.as_view(), name='api-class-subject-create'),
    path('subject/update/<int:id>', views.ClassSubjectUpdateAPIView.as_view(), name='api-class-subject-update'),
    path('subject/destroy/<int:id>', views.ClassSubjectDestroyAPIView.as_view(), name='api-class-subject-destroy'),
    path('member/create', views.ClassMemberCreateAPIView.as_view(), name='api-class-member-create'),
    path('member/update/<int:id>', views.ClassMemberUpdateAPIView.as_view(), name='api-class-member-update'),
    path('member/destroy/<int:id>', views.ClassMemberDestroyAPIView.as_view(), name='api-class-member-destroy'),

]