# accounts/urls.py
from django.urls import path

from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls import include, url


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('initial/', TemplateView.as_view(template_name = "initial.html"), name = 'initial'),
    path('survey/index/', views.IndexView.as_view(), name="index"),
    path('survey/new/', views.BuildView.as_view(), name="survey_create"),
    path('survey/new/creation-success/', views.SuccessView.as_view(), name="survey_creation_success"),
    path('survey/<int:survey_id>/', views.SurveyDetailView.as_view(), name="survey_detail"),
    path('survey/<int:survey_id>/edit/', views.SurveyEditView.as_view(), name="survey_edit"),
    path('survey/<int:survey_id>/response/', views.RespondView.as_view(), name="survey_respond"),
    path('survey/<int:survey_id>/response/<int:response_id>/', views.RespondView.as_view(), name="response")
]
