from django.contrib import admin

# Register your models here.
from .models import PYQ, Book, TimeTable, Assignment, Calender

admin.site.register(PYQ)
admin.site.register(Book)
admin.site.register(TimeTable)
admin.site.register(Assignment)
admin.site.register(Calender)