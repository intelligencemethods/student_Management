# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Student, Teacher,Subject

# Register your models here.



class TeacherAdmin(admin.ModelAdmin):
    '''Admin View for Teacher'''

    list_display = (
        'full_name',
        'gender',
    )

    list_filter = (
        'gender',
    )

    list_select_related = True
    raw_id_fields = ('user',)

    search_fields = (
        'user__first_name',
        'user__last_name',
    )

    ordering = ('-date_of_joining',)

admin.site.register(Student)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Subject)