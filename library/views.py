from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Author, Book
from .forms import AuthorForm, BiblioForm1, BiblioForm2, BiblioForm3
from django.views.generic.edit import FormView

from django.shortcuts import render
from formtools.wizard.views import SessionWizardView


class AuthorList(ListView):
    model = Author
    template_name = 'authors/author_list.html'


class AuthorCreate(CreateView):
    model = Author
    fields = ['name', 'email']
    template_name = 'authors/author.html/'
    success_url = reverse_lazy('library:author_list')


class FormWizardView(SessionWizardView):
    template_name = "wizard.html"
    form_list = [BiblioForm1, BiblioForm2, BiblioForm3]

    def done(self, form_list, **kwargs):
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

def get(self, request, *args, **kwargs):
    try:
        return self.render(self.get_form())
    except KeyError:
        return super().get(request, *args, **kwargs)
