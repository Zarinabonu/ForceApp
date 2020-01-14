from django.urls import include, path

urlpatterns = [
    path('parent/', include('app.api.parent.urls')),
    path('student/', include('app.api.student.urls')),
    path('teacher/', include('app.api.teacher.urls')),
    path('class/', include('app.api.class_.urls')),
    path('subject/', include('app.api.subject.urls')),

]