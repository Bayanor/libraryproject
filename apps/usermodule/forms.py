from django import forms
from django.contrib.auth.models import User

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


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    username = forms.CharField(label="Username", max_length=150, required=True)
    email = forms.EmailField(label="Email", required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput, required=True)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('The two passwords do not match.')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        # set_password hashes the password (PBKDF2 + SHA256) instead of storing it raw
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=150, required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
