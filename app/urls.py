from django.urls import path
from app import views

urlpatterns = [
    # path('', views.hello, name='home_root'),
    path('job/<int:id>', views.job_details, name='job_details'),
    path('', views.job_list, name='jobs_home'),
]