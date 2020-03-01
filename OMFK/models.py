from django.db import models

STAFF_STATUS_CHOICES = (
    ("1", "Full Time"),
    ("2", "Part Time"),
    ("3", "Volunteer"),
)

class Staff(models.Model):
    staff_ID = models.IntegerField(max_length=250)
    staff_Last_Name = models.CharField(max_length=250)
    staff_First_Name = models.CharField(max_length=250)
    staff_Street_Address = models.CharField(max_length=1024)
    staff_City = models.CharField(max_length=1024)
    staff_Zipcode = models.IntegerField(max_length=250)
    staff_Email = models.EmailField(max_length=1024)
    staff_Phone = models.IntegerField(max_length=1024)
    staff_status = models.CharField(max_length=100, choices = STAFF_STATUS_CHOICES, default = 'Fulltime')

class Student(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    student_ID = models.IntegerField(max_length=250)
    student_Last_Name = models.CharField(max_length=250)
    student_First_Name = models.CharField(max_length=250)
    student_Date_of_Birth = models.DateField()
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    student_Gender = models.IntegerField(choices=GENDER_CHOICES)
    student_Street_Address = models.CharField(max_length=1024)
    student_City = models.CharField(max_length=1024)
    student_Zipcode = models.IntegerField(max_length=250)
    student_Email = models.EmailField(max_length=1024)
    student_Phone = models.IntegerField(max_length=1024)
    student_School = models.CharField(max_length=1024)
    student_Notes = models.CharField(max_length=1024)

