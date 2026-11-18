from django import forms
from .models import Address, Student, Student2


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']

    name = forms.CharField(label="Name", max_length=50, required=True)
    age = forms.IntegerField(label="Age", required=True)
    address = forms.ModelChoiceField(
        label="Address",
        queryset=Address.objects.all().order_by("city"),
        empty_label="Select a city",
    )

    def clean_age(self):
        age = self.cleaned_data['age']
        if age <= 3:
            raise forms.ValidationError('Age must be above 3.')
        return age


class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']

    name = forms.CharField(label="Name", max_length=50, required=True)
    age = forms.IntegerField(label="Age", required=True)
    addresses = forms.ModelMultipleChoiceField(
        label="Addresses",
        queryset=Address.objects.all().order_by("city"),
        widget=forms.CheckboxSelectMultiple(),
    )

    def clean_age(self):
        age = self.cleaned_data['age']
        if age <= 3:
            raise forms.ValidationError('Age must be above 3.')
        return age
