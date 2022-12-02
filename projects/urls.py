from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='Project_list'),
    path('project/create', views.ProjectCreateView.as_view(), name='Project_create'),
]