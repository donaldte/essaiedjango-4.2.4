from django.contrib import admin
from .models import Contact, Newsletter, Course, DeleteStudent, Service, Plan, Subcribe, Student

# Register your models here.

admin.site.register(Contact)
admin.site.register(Newsletter)
admin.site.register(Service)
admin.site.register(Plan)

admin.site.register(Subcribe)
admin.site.register(Student)
admin.site.register(DeleteStudent)
admin.site.register(Course)

