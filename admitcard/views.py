
from .forms import AdmitCardForm, CourseFormSet
from django.shortcuts import render, redirect
from .models import AdmitCard, Course  # Import Course model
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from weasyprint import HTML


# Admit card form view
def admit_card_form(request):
    if request.method == 'POST':
        admit_form = AdmitCardForm(request.POST, request.FILES)
        course_formset = CourseFormSet(request.POST)

        if admit_form.is_valid() and course_formset.is_valid():
            admit_card = admit_form.save(commit=False)
            admit_card.save()

            for course_form in course_formset:
                if course_form.is_valid():
                    course = course_form.save()
                    admit_card.courses.add(course)

            admit_card.save()
            
            # Redirect to the preview page where user can download PDF
            return redirect('admit_preview', admit_card_id=admit_card.id)

        else:
            print("Admit Form Errors:", admit_form.errors)
            print("Course Formset Errors:", course_formset.errors)

    else:
        admit_form = AdmitCardForm()
        course_formset = CourseFormSet(queryset=Course.objects.none())

    return render(request, 'admitcard/form.html', {
        'admit_form': admit_form,
        'course_formset': course_formset,
    })

# Preview page where user can download the PDF
def admit_preview(request, admit_card_id):
    admit_card = get_object_or_404(AdmitCard, id=admit_card_id)
    return render(request, 'admitcard/admit_preview.html', {'admit_card': admit_card})

# Generate the PDF and download
def generate_admit_card_pdf(request, admit_card_id):
    admit_card = get_object_or_404(AdmitCard, id=admit_card_id)

    # Render the admit card to an HTML template
    html_content = render(request, 'admitcard/admit_card_pdf_template.html', {
        'admit_card': admit_card
    })

    # Convert the HTML to PDF using WeasyPrint
    pdf_file = HTML(string=html_content.content).write_pdf()

    # Create a response object and set the content type to PDF
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="admit_card_{admit_card.student_code}.pdf"'
    return response
