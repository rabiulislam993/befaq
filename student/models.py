from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Max

from madrasa.models import Madrasa

REGISTRATION_YEARS = (
    ('2016', '2016'),
    ('2017', '2017'),
    ('2018', '2018'),
)

MARHALA = [
    ('takmil', 'Takmil'),
    ('fazilat', 'Fazilat'),
    ('hifz', 'Hifzul Quran'),
]

SUBJECT_LIST = {
    'takmil':['bukhari','muslim','tirmizi'],
    'fazilat':['meshkat','hedaya','nukhbah'],
    'hifz':['quran','tazbid'],
}

class Student(models.Model):
    reg_id        = models.PositiveIntegerField(blank=True)
    reg_year      = models.CharField(max_length=4,
                                     choices=REGISTRATION_YEARS,
                                     default='2017')
    name          = models.CharField(max_length=100)
    father        = models.CharField(max_length=100)
    address       = models.TextField(blank=True, null=True)
    madrasa       = models.ForeignKey(Madrasa, on_delete=models.CASCADE, related_name='students')
    marhala       = models.CharField(max_length=10,
                                     choices=MARHALA)
    registrar     = models.ForeignKey('auth.User', default=1)
    registered_at = models.DateTimeField(auto_now_add=True)

    is_rejected   = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('website:student_detail', kwargs={'reg_id':self.reg_id,
                                                           'reg_year':self.reg_year})

    def get_subject_list(self):
        subject_list = SUBJECT_LIST[self.marhala]
        return subject_list

    def get_result(self):
        try:
            return self.result
        except:
            return None

    def __str__(self):
        return '{} ({})'.format(self.name, self.reg_id)

    def save(self, *args, **kwargs):
        if self.reg_id:
            return super(Student, self).save(*args, **kwargs)

        reg_year = self.reg_year
        last_reg_id_of_this_year = Student.objects.filter(reg_year=reg_year).aggregate(Max('reg_id'))
        if last_reg_id_of_this_year['reg_id__max']:
            self.reg_id = 1 + last_reg_id_of_this_year.get('reg_id__max', 0)
        else:
            self.reg_id = 1

        return super(Student, self).save(*args, **kwargs)

