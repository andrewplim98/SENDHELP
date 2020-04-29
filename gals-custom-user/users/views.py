from django.shortcuts import render
from .forms import CustomUserCreationForm
#from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views import View
from django.views.generic import TemplateView

from django.urls import reverse
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from dynamic_forms.views import DynamicFormMixin
from .models import Survey, SurveyResponse

#kyle 1
# from .myForm import myForm

# #kyle 2
# from django.http import HttpResponse
# #from .forms import CreatePollForm
# from .models import Poll


class SignUp(generic.CreateView):
    #form_class = UserCreationForm
    form_class = CustomUserCreationForm

    #register(CustomUser, CustomUserAdmin)
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Initial(TemplateView):
    template_name = 'initial.html'



class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['surveys'] = Survey.objects.all()
        return context


class BuildView(CreateView):
    model = Survey
    fields = '__all__'
    template_name = "build.html"
    def get_success_url(self):
        return reverse('survey_creation_success')


class SuccessView(TemplateView):
    template_name = "survey_creation_success.html"


class SurveyDetailView(DetailView):
    model = Survey
    pk_url_kwarg = "survey_id"
    template_name = "survey_detail.html"


class SurveyEditView(UpdateView):
    model = Survey
    fields = '__all__'
    pk_url_kwarg = "survey_id"
    template_name = "survey_edit.html"

    def get_success_url(self):
        return reverse('survey_detail', kwargs={"survey_id": self.object.pk})


class RespondView(DynamicFormMixin, CreateView):
    model = SurveyResponse
    fields = ['response']
    template_name = "respond.html"

    form_model = Survey
    form_pk_url_kwarg = "survey_id"
    response_form_fk_field = "survey"
    response_field = "response"

    def get_success_url(self):
        return reverse('survey_detail', kwargs={"survey_id": self.form_instance.pk})

# def kyleview(request):
#     f=myForm()
#     return render(request, 'kyle.html', {'form':f})
#
# def showkyleview(request):
#     rec_form=myForm(request.POST)
#     b_f=rec_form['c_field'] #name of field variable
#     dct={
#         'auto_id' : b_f.auto_id,
#         'data' : b_f.data,
#         'errors' : b_f.errors,
#         'field' : b_f.field,
#         'form' : b_f.form,
#         'help_text' : b_f.help_text,
#         'html_name' : b_f.html_name,
#         'id_for_label' : b_f.id_for_label,
#         'is_hidden' : b_f.is_hidden,
#         'label' : b_f.label,
#         'name' : b_f.name
#     }
#     return render(request,'showkyle.html',{'data':dct})
