from django.urls import path
from . import views

app_name = 'jobs'
urlpatterns = [
    path('', views.job_list, name='index'),
    path('job_detail/<int:job_id>/', views.job_detail, name='job_detail'),
    path('resume/add/', views.ResumeCreateView.as_view(), name='resume_add'),
    path('resume/<int:pk>/', views.ResumeDetailView.as_view(), name='resume_detail'),
]
