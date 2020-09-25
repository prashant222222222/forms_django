from django import forms
from main import models


class example(forms.Form):
    # not necessaty to give maxlength becz not connectec to database directly
    name = forms.CharField(max_length=256)
    about_me = forms.CharField(widget=forms.Textarea())
    active = forms.BooleanField()

# if changes in model and needed to change in form too so meta


class StudentForm(forms.ModelForm):
    random = forms.CharField(max_length=256)  # fied not in model

    class Meta:
        model = models.Student
        fields = '__all__'  # ('name','') // only particular fields are needed
