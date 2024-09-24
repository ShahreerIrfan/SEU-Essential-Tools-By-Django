from django.shortcuts import render,HttpResponse

# Create your views here.

from django.shortcuts import render, redirect
from .forms import AdmitCardForm, CourseFormSet
from .models import AdmitCard

from django.shortcuts import render, redirect
from .forms import AdmitCardForm, CourseFormSet
from .models import AdmitCard, Course  # Import Course model

from django.shortcuts import render, redirect
from .forms import AdmitCardForm, CourseFormSet
from .models import AdmitCard



def admit_card_form(request):
    if request.method == 'POST':
        admit_form = AdmitCardForm(request.POST, request.FILES)
        course_formset = CourseFormSet(request.POST)

        # Check if both forms are valid
        if admit_form.is_valid() and course_formset.is_valid():
            # Save the admit card (but don't commit yet)
            admit_card = admit_form.save(commit=False)
            admit_card.save()

            # Loop through the formset and save valid forms
            for course_form in course_formset:
                if course_form.is_valid():  # Ensure form is valid
                    if course_form.cleaned_data.get('course_code') and course_form.cleaned_data.get('course_name'):
                        course = course_form.save()
                        admit_card.courses.add(course)

            admit_card.save()  # Save the admit card after adding courses

            return redirect('success')  # Redirect to a success page after saving

        else:
            print("Admit Form Errors:", admit_form.errors)
            print("Course Formset Errors:", course_formset.errors)

    else:
        admit_form = AdmitCardForm()
        course_formset = CourseFormSet(queryset=Course.objects.none())  # Initially empty

    return render(request, 'admitcard/form.html', {
        'admit_form': admit_form,
        'course_formset': course_formset,
    })







