from django.db import models

# Model for Course
class Course(models.Model):
    course_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.course_code} - {self.course_name}'

# Model for Admit Card
class AdmitCard(models.Model):
    # 1. Student Code (13-digit numeric input)
    student_code = models.CharField(max_length=13)

    # 2. Name (text input)
    name = models.CharField(max_length=100)

    # 3. Courses - Many-to-Many Relationship with Course model
    courses = models.ManyToManyField(Course)

    # 4. Image for Admit Card (photo upload)
    image = models.ImageField(upload_to='admitcard_images/')

    # 5. Examination Type (dropdown with Midterm or Final)
    EXAM_TYPE_CHOICES = [
        ('Midterm Examination', 'Midterm Examination'),
        ('Final Examination', 'Final Examination'),
    ]
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE_CHOICES)

    # 6. Semester Name (dropdown with Spring, Summer, Fall)
    SEMESTER_CHOICES = [
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Fall', 'Fall'),
    ]
    semester_name = models.CharField(max_length=10, choices=SEMESTER_CHOICES)

    # New field: Year of the semester
    year = models.IntegerField(null=True)

    # 7. Program Name (dropdown with BSc in CSE and other departments)
    PROGRAM_CHOICES = [
        ('BSc in CSE', 'BSc in CSE'),
        ('BSc in EEE', 'BSc in EEE'),
        ('BBA', 'BBA'),
        ('MBA', 'MBA'),
    ]
    program_name = models.CharField(max_length=50, choices=PROGRAM_CHOICES)

    # 8. Batch Number (numeric input)
    batch_number = models.IntegerField()

    def __str__(self):
        return f'{self.student_code} - {self.name}'

