from django.urls import path
from .views import JobLoginView,RegisterPage,JobPost,JobCreate,JobUpdate,JobDelete,JobList,Jobdetail
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',JobLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('',JobPost.as_view(),name='Jobposts'),
    path('Job/<int:pk>/',Jobdetail.as_view(),name='JobPost'),
    path('Job-create/',JobCreate.as_view(),name = 'Job-create'),
    path('Job-update/<int:pk>/',JobUpdate.as_view(),name='Job-update'),
    path('Job-delete/<int:pk>/',JobDelete.as_view(),name='Job-delete'),
]
 