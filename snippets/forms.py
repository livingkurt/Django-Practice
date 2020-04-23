from django import forms

class SnippetForm(forms.Form):

    title = forms.CharField(label='Title', max_length=256)
    
    snippet = forms.CharField(label='Snippet', max_length=256)

    language = forms.CharField(label='Language', max_length=256)

    description = forms.CharField(label='Description', max_length=256)
