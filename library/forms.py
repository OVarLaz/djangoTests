from django import forms
from library.models import Biblioteca

class AuthorForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

class BiblioForm1(forms.ModelForm):

    class Meta:
        model = Biblioteca
        fields = ['biblio', 'author', 'title']

    def __init__(self, *args, **kwargs):
        super(BiblioForm1, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class BiblioForm2(forms.ModelForm):

    class Meta:
        model = Biblioteca
        fields = ['sbs', 'colegio', 'enfermeria']

    def __init__(self, *args, **kwargs):
        super(BiblioForm2, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class BiblioForm3(forms.ModelForm):

    class Meta:
        model = Biblioteca
        fields = ['bodega', 'name', 'email']

    def __init__(self, *args, **kwargs):
        super(BiblioForm3, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })