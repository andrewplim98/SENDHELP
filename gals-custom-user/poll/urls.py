from django.urls import path

from poll import views as poll_views

urlpatterns = [
    path('home/homekyle/', poll_views.homekyle, name='homekyle'),
    path('home/create/', poll_views.create, name='create'),
    path('home/vote/<poll_id>/', poll_views.vote, name='vote'),
    path('home/results/<poll_id>/', poll_views.results, name='results'),
]
