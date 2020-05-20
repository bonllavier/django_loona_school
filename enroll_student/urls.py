from django.urls import path, include

from enroll_student.views import Updateuserclass, AddTeacherSubject, TeacherSubjectList

urlpatterns = [
    path('<int:pk>', Updateuserclass.as_view(), name='enroll_student'),
    path('subject_list/', TeacherSubjectList.as_view(), name='enroll_teacher_subjects'),
    path('subject_list/add/<int:pk>', AddTeacherSubject.as_view(), name='enroll_teacher'),
]
