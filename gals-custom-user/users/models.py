from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

from .managers import CustomUserManager
from dynamic_forms.models import FormField, ResponseField
from django import forms



class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(unique = True, max_length = 50)
    last_name = models.CharField(unique = True, max_length = 50)
    eagle_id = models.CharField(max_length = 9, primary_key=True)
    is_instructor = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
#WIP, comment this out if you're doing something else
class Course(models.Model):
    course_name = models.CharField(max_length = 30)
    course_id = models.CharField(unique = True, max_length = 12, primary_key = True)
    course_date = models.CharField(max_length = 10)
    course_section = models.CharField(max_length = 3)
    course_semester = models.CharField(max_length = 10)
# #
class CourseInstructor(models.Model):
    course = models.ManyToManyField(Course)
    eagle_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
# #

# #

class CourseTeam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(unique = True, max_length = 50)

class CourseStudent(models.Model): 
    course = models.ManyToManyField(Course)
    eagle_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    team = models.ManyToManyField(CourseTeam)
# #


# ???

# class Assessment(models.Model):
#
#     #creator = models.ForeignKey(CustomUser.eagle_id, on_delete=models.CASCADE)
#     creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     assessment_id = models.CharField(unique = True, primary_key = True, max_length = 9)
#     #group = models.ForeignKey(CourseTeam.name, on_delete=models.CASCADE)
#     group = models.ForeignKey(CourseTeam, on_delete=models.CASCADE)

# #
# # #probably broken
# # #class AssessmentMCQ(models.Model):
# # #    choices = (("1", "Strongly Agree"), ("2", "Agree"), ("3", "Neither Agree or Disagree"), ("4", "Disagree"), ("5", "Strongly Disagree"))
# #

# is deprecated the word?

# class AssessmentOEQ(models.Model):
#     question = models.CharField(max_length = 250)
#     answer = models.CharField(max_length = 250)
#     #assessment = models.ForeignKey(Assessment.assessment_id, on_delete=models.CASCADE)
#     assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)


# CLASS_CHOICES = (
#     ('SWE','SWE'),
#     ('CS1', 'CS1'),
#     ('CS2','CS2'),
#     ('Randomness','Randomness'),
#     ('Logic','Logic'),
# )

class Survey(models.Model):
    startdate = models.DateTimeField(default = now)
    enddate = models.DateTimeField(default = now)
    topic = models.CharField(max_length=100)
    course_survey = models.ManyToManyField(Course)
    #start_date = models.DateField(default='')
    #submission_date = models.DateField(default='')
    form = FormField()
    def __str__(self):
        return "Survey #{}: ".format(self.pk, self.topic)


class SurveyResponse(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    response = ResponseField()
