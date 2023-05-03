from django.urls import path
from .views import (
    JobLoginView, RegisterPage, JobCreate,
    JobUpdate, JobDelete, Jobdetail, JobPostView, JobList, JobDec
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', JobLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    # path('', JobList.as_view(), name='Jobposts'),
    path('', JobPostView.as_view(), name='Jobview'),
    path('Job/<int:pk>/', Jobdetail.as_view(), name='JobPost'),
    path('job-create/', JobCreate.as_view(), name='job-create'),
    path('jobupdate/<int:pk>/', JobUpdate.as_view(), name='jobupdate'),
    path('jobdelete/<int:pk>/', JobDelete.as_view(), name='jobdelete'),
    path('demo/', JobDec.as_view(), name='jobdemo') 
]
