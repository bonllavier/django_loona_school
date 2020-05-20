from django.urls import path, include


from grades.views import UpdateUserGrade

urlpatterns = [
    path('<int:pk>', UpdateUserGrade.as_view(), name='grade'),
]
