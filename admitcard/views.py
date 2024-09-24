from .forms import AdmitCardForm, CourseFormSet
from .models import AdmitCard, Course  
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from datetime import datetime
import io
import qrcode


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



def admit_preview(request, admit_card_id):
    admit_card = get_object_or_404(AdmitCard, id=admit_card_id)
    return render(request, 'admitcard/admit_preview.html', {'admit_card': admit_card})



def generate_admit_card_pdf(request, admit_card_id):
    admit_card = AdmitCard.objects.get(pk=admit_card_id)

   
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Admit_Card_{admit_card.student_code}.pdf"'


    doc = SimpleDocTemplate(response, pagesize=A4)

 
    styles = getSampleStyleSheet()
    elements = []

  
    qr_code_img = qrcode.make(admit_card.student_code)
    qr_code_buffer = io.BytesIO()
    qr_code_img.save(qr_code_buffer)
    qr_code_image = Image(qr_code_buffer, width=1.2 * inch, height=1.2 * inch)


    if admit_card.image:
        student_image = Image(admit_card.image.path, width=1.2 * inch, height=1.2 * inch)
    else:
        student_image = None


    header_text = '''
    <font size=16><b>SOUTHEAST UNIVERSITY</b></font><br/>
    <font size=10>252, Tejgaon I/A, Dhaka 1208, Bangladesh</font><br/><br/>
    <font size=14><b>Admit Card</b></font><br/>
    <font size=12>Mid Term Examination</font><br/>
    <font size=12>{} {}</font><br/>
    '''.format(admit_card.semester_name, admit_card.year)
    elements.append(Paragraph(header_text, styles['Title']))
    elements.append(Spacer(1, 12))


    student_qr_table = Table([
        [qr_code_image, '', student_image]
    ], colWidths=[1.5 * inch, 4.5 * inch, 1.5 * inch])
    elements.append(student_qr_table)
    elements.append(Spacer(1, 12))

 
    student_info = [
        ['Student Code', f"{admit_card.student_code}"],
        ['Name', f"{admit_card.name}"],
        ['Program', f"{admit_card.program_name}, Batch #{admit_card.batch_number}"]
    ]
    student_table_style = TableStyle([
        ('BACKGROUND', (0, 0), (1, 0), colors.lightgrey),
        ('BOX', (0, 0), (-1, -1), 2, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ])
    student_table = Table(student_info, colWidths=[2 * inch, 4 * inch])
    student_table.setStyle(student_table_style)
    elements.append(student_table)
    elements.append(Spacer(1, 24))

    
    courses_data = [['Course Code', 'Course Title', 'Registration Type', 'Invigilator’s Signature']]
    for course in admit_card.courses.all():
        courses_data.append([course.course_code, course.course_name, 'Regular', ''])

    course_table = Table(courses_data, colWidths=[1.5 * inch, 3 * inch, 1.5 * inch, 2 * inch])
    course_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    elements.append(course_table)
    elements.append(Spacer(1, 24))

    
    footer_info = f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} This file was generated from UMS without any alteration or erasure."
    elements.append(Paragraph(footer_info, styles['Normal']))

  
    instructions_title = "Instructions to the Examinee:"
    instructions_text = '''
    - Print this Admit Card on an A4 size paper. Colour print is not mandatory.
    - Admit card is valid only if the examinee photograph is legibly printed.
    - The examinee must bring the ‘Admit Card’ and ‘Student ID’ at the examination hall and show those to the invigilators when they ask.
    - The examinee must arrive in the examination hall at least 15 minutes before the start of the examination.
    - The examinee must comply with the directions given by the invigilators at the examination hall.
    - Use of cell phones, programmable calculators, smartwatches and other electronic devices are prohibited in the examination hall.
    - The examinee involved in unfair means/misconduct in the examination hall will be expelled from the examination.
    '''
    elements.append(Spacer(1, 24))
    elements.append(Paragraph(instructions_title, styles['Heading2']))
    elements.append(Paragraph(instructions_text, styles['Normal']))

 
    doc.build(elements)

    return response
