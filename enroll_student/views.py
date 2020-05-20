from django.shortcuts import render
from django.views.generic import UpdateView, ListView
from users.models import CustomUser
from classroom.models import ClassRoom, Subjects, Grades
from django.shortcuts import redirect
from django.urls import reverse_lazy
# Create your views here.


class Updateuserclass(UpdateView):
    model = CustomUser
    fields = ['fk_idclassroom']
    #form_class = NoteForm
    template_name = 'enroll/enroll_stu.html'



    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['classroom_list'] = ClassRoom.objects.all()
        return context

    def get_success_url(self):

        actual_user = CustomUser.objects.get(id=self.request.user.id)
        subject_list = Subjects.objects.all()
        for subject in subject_list:
            grade = Grades(fk_idsubject=Subjects.objects.get(id=subject.id), fk_iduser=actual_user)
            grade.save()
        return reverse_lazy('classroom')

class AddTeacherSubject(UpdateView):
    model = Subjects
    fields = ['fk_idteacher']
    #form_class = NoteForm
    template_name = 'enroll/enroll_teacher.html'
    context_object_name = 'subject_list'



    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['subject_list'] = Subjects.objects.get(id=)
    #     return context

    def get_success_url(self):
        return reverse_lazy('classroom')

class TeacherSubjectList(ListView):
    model = Subjects
    template_name = 'enroll/subject_list.html'
    context_object_name = 'subject_list' # new