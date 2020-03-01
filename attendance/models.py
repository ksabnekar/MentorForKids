from django.db import models
from OMFK.models import Staff
from OMFK.models import Student

ATTENDANCE_CHOICES = (
    ("1", "PRESENT"),
    ("2", "ABSENT"),
    ("3", "LATE"),
)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    meeting_date = models.DateField()
    meeting_time = models. TimeField()
    attendance = models.CharField(max_length=1024, choices = ATTENDANCE_CHOICES, default = 'PRESENT' )
    notes = models.CharField(max_length=1024)


