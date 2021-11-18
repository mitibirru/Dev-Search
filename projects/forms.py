from django import forms
from django import forms
from django.forms import ModelForm
from .models import Project, Review

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'Tags']
        widgets = {
            'Tags': forms.CheckboxSelectMultiple(),
        }
    
    def __init__(self, *args, **kargs):
        super(ProjectForm, self).__init__(*args, **kargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }

    def __init__(self, *args, **kargs):
        super(ReviewForm, self).__init__(*args, **kargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})