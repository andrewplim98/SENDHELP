from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Course
from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email','first_name','last_name','eagle_id', 'is_staff')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class CourseAddForm(ModelForm):
    class Meta:
        model = Course
        fields = ('course_name', 'course_id', 'course_date', 'course_section', 'course_semester',)



