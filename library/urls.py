from django.urls import path
from .views import *
from .forms import AuthorForm, BiblioForm1, BiblioForm2, BiblioForm3

urlpatterns = [
    # [...]
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('author/add/', AuthorCreate.as_view(), name='author-add'),
    path('wizard/', FormWizardView.as_view([BiblioForm1, BiblioForm2, BiblioForm3])),
]