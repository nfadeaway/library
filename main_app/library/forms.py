from django import forms
from library.models import Author, Book


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

        widgets = {
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class AddBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

        widgets = {
            'publication_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

