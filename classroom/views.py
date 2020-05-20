from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from classroom.models import ClassRoom, Subjects
# class ClassMainPage(TemplateView):
#     model = ClassRoom
#     template_name = 'classroom/main.html'
#     context_object_name = 'all_classroom_list' # new

class ClassMainPage(ListView):
    #model = Subjects
    template_name = 'classroom/main.html'
    context_object_name = 'all_subjects_list' # new
    # context_object_name = 'book_list'
    # queryset = Subjects.objects.filter(publisher__name='ACME Publishing')
    # template_name = 'books/acme_list.html'
    def get_queryset(self):
        return Subjects.objects.filter(fk_idteacher=self.request.user.id)

class ClassMainPageDetail(DetailView):
    model = Subjects
    template_name = 'classroom/main.html'

    def get_context_data(self):
        print("entered context")
        context = super(ClassMainPageDetail, self).get_context_data(**kwargs)
        context['subjects_by_teacher'] = Subjects.objects.filter(fk_idteacher=self.request.user.id)
        #context['subjects_by_student'] = Subjects.objects.filter(fk_idclassroom=self.request.user.fk_idclassroom)
        return context

def ClassMainPage2(request):
    '''Se renderiza la pagina donde se analiza la URL'''
    my_context = {
        "subjects_by_teacher" : Subjects.objects.filter(fk_idteacher=request.user.id),
        "subjects_by_student" : Subjects.objects.filter(fk_idclassroom=request.user.fk_idclassroom)
    }
    return render(request, 'classroom/main.html', my_context)

class SubjectPageDetail(TemplateView):
    template_name = 'classroom/subject.html'