from django.urls import path, include

from classroom.views import SubjectPageDetail, ClassMainPageDetail
from . import views

urlpatterns = [
    path('', views.ClassMainPage2, name='classroom'),
    path('enroll/', include('enroll_student.urls')),
]
