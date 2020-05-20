from django.shortcuts import render
from classroom.models import ClassRoom, Subjects, Grades
from users.models import CustomUser
from django.db.models import Q
# Create your views here.

def subject_detail(request, id):
    actual_subject_fk_classroom = Subjects.objects.get(id=id).fk_idclassroom.id
    student_list = CustomUser.objects.filter(fk_idclassroom=actual_subject_fk_classroom)
    print("//Student list")
    new_student_w_grade = []
    for student in student_list:
        print("//consutla id grade")
        grade_id = Grades.objects.filter(fk_idsubject=id).filter(fk_iduser=student.id)
        print(grade_id)
        print("/////")
        new_student_w_grade.append([student,grade_id])


    print("///classroom id")
    print(actual_subject_fk_classroom)
    print("/////")
    # my_context = {
    #     "subject_info" : Subjects.objects.get(id=id),
    #     "student_list" : CustomUser.objects.filter(fk_idclassroom=actual_subject_fk_classroom),
    #     "grades_by_student" :  Grades.objects.filter(fk_idsubject=id).filter(fk_iduser=request.user.id),
    # }
    my_context = {
        "subject_info" : Subjects.objects.get(id=id),
        "student_list" : new_student_w_grade,
        "grades_by_student" :  Grades.objects.filter(fk_idsubject=id).filter(fk_iduser=request.user.id),
    }
    return render(request, 'subject/main.html', my_context)
    #do something with this user
