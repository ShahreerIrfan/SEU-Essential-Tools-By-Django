from django import forms
from .models import AdmitCard, Course
from django.forms import modelformset_factory


class AdmitCardForm(forms.ModelForm):
    class Meta:
        model = AdmitCard
        fields = ['student_code', 'name', 'batch_number', 'exam_type', 'semester_name', 'year', 'program_name', 'image']
        widgets = {
            'student_code': forms.TextInput(attrs={
                'class': 'block w-full mt-2 p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-300',
                'placeholder': 'Enter Student Code'
            }),
            'name': forms.TextInput(attrs={
                'class': 'block w-full mt-2 p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-300',
                'placeholder': 'Enter Name'
            }),
            'batch_number': forms.NumberInput(attrs={
                'class': 'block w-full mt-2 p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-300',
                'placeholder': 'Enter Batch Number'
            }),
            'exam_type': forms.Select(attrs={
                'class': 'block w-full mt-2 p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-300',
            }),
            'semester_name': forms.Select(attrs={
                'class': 'block w-full mt-2 p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-300',
            }),
            'year': forms.NumberInput(attrs={
                'class': 'block w-full mt-2 p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-300',
                'placeholder': 'Enter Year'
            }),
            'program_name': forms.Select(attrs={
                'class': 'block w-full mt-2 p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-300',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'block w-full mt-2 p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-300',
            }),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_code', 'course_name']

        widgets = {
            'course_code': forms.TextInput(attrs={
                'placeholder': 'Enter Course Code',
                'class': 'block w-full mt-1 p-2 border border-gray-300 rounded-md'
            }),
            'course_name': forms.TextInput(attrs={
                'placeholder': 'Enter Course Name',
                'class': 'block w-full mt-1 p-2 border border-gray-300 rounded-md'
            }),
        }


CourseFormSet = modelformset_factory(Course, form=CourseForm, extra=1)
