from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    is_deleted = models.PositiveSmallIntegerField(default=0)

# here we are adding is_del functionality
# here the below code is to show the name of the student in admin panel instead of student.object(this called as overwritting method)

    def __str__(self):
        return self.name
