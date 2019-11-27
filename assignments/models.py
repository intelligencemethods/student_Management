# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from schoolApp.utils import GENDER_CHOICES
from django.contrib.auth.models import User
# Create your models here.
class Subject(models.Model):
    subject_name=models.CharField(max_length = 100)
    def ____(self):
        return self.subject_name

    class Meta:
        db_table="subject"   
        
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_joining = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    teacher=models.ManyToManyField(Subject)
    class Meta:
        """Meta definition for Teacher."""

        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    @property
    def full_name(self):
        """Returns full name of teacher"""
        return self.__str__()

    def __unicode__(self):
        """Unicode representation of Teacher."""
        return '{} {}'.format(self.user.first_name, self.user.last_name)
        
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_no = models.IntegerField(unique=True)
    student_name=models.CharField(max_length=13)
    standard=models.CharField(max_length=13)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    teacher=models.ManyToManyField(Teacher)
    class Meta:
        """Meta definition for Teacher."""

        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    @property
    def full_name(self):
        """Returns full name of teacher"""
        return self.__str__()

    def __str__(self):
        """Unicode representation of Teacher."""
        return '{} {}'.format(self.user.first_name, self.user.last_name)


        
     

 
        


