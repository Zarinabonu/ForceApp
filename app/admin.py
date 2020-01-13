from django.contrib import admin
from .model import Account, Attandance, Class, ClassMember, ClassSubject, Comment, Marks, Notification, Notifications, Parent, Student, Subject, Quater, Teacher

admin.site.register(Account)
admin.site.register(Attandance)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(ClassMember)
admin.site.register(ClassSubject)
admin.site.register(Marks)
admin.site.register(Notification)
admin.site.register(Notifications)
admin.site.register(Parent)
admin.site.register(Subject)
admin.site.register(Quater)

# Register your models here.
