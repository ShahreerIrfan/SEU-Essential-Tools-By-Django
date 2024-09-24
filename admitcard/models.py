from django.db import models


class Course(models.Model):
    course_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.course_code} - {self.course_name}'


class AdmitCard(models.Model):

    student_code = models.CharField(max_length=13)

  
    name = models.CharField(max_length=100)

  
    courses = models.ManyToManyField(Course)

 
    image = models.ImageField(upload_to='admitcard_images/')

 
    EXAM_TYPE_CHOICES = [
        ('Midterm Examination', 'Midterm Examination'),
        ('Final Examination', 'Final Examination'),
    ]
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE_CHOICES)

  
    SEMESTER_CHOICES = [
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Fall', 'Fall'),
    ]
    semester_name = models.CharField(max_length=10, choices=SEMESTER_CHOICES)


    year = models.IntegerField(null=True)


    PROGRAM_CHOICES = [
        ('BSc in CSE', 'BSc in CSE'),
        ('BSc in EEE', 'BSc in EEE'),
        ('BBA', 'BBA'),
        ('MBA', 'MBA'),
    ]
    program_name = models.CharField(max_length=50, choices=PROGRAM_CHOICES)

   
    batch_number = models.IntegerField()

    def __str__(self):
        return f'{self.student_code} - {self.name}'

