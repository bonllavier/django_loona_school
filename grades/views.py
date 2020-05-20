from django.shortcuts import render
from classroom.models import Grades, Subjects
from django.views.generic import UpdateView
from grades.forms import GradesForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
# Create your views here.

class UpdateUserGrade(UpdateView):
    model = Grades
    form_class = GradesForm
    #fields = ['first_trimester','second_trimester','third_trimester','final_exam']
    #form_class = NoteForm
    template_name = 'grade/main.html'

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['grades'] = Grades.objects.get(id=self.kwargs['pk'])
    #     return context

    def get_success_url(self):
        return reverse_lazy('classroom')