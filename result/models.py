from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

from student.models import Student


class Result(models.Model):
    student    = models.OneToOneField(Student, on_delete=models.CASCADE)

    subject_1  = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
    subject_2  = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
    subject_3  = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
    subject_4  = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
    subject_5  = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
    subject_6  = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
    subject_7  = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
    subject_8  = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
    subject_9  = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
    subject_10 = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])

    def __str__(self):
        return 'result of {} ({})'.format(self.student.name, self.student.reg_id)

    def get_absolute_url(self):
        return reverse('website:student_detail', kwargs={'reg_id':self.student.reg_id,
                                                           'reg_year':self.student.reg_year})
