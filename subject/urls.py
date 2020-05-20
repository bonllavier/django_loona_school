from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:id>', views.subject_detail, name='subject'),
    path('grade/', include('grades.urls')),
]
