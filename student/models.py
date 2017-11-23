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
    ('sanabia', 'Sanabia Ulia'),
    ('mutawassitah', 'Mutawassitah'),
    ('ibtedaiyah', 'Ibtedaiyah'),
    ('hifz', 'Hifzul Quran'),
    ('tazbid', 'Ilmut Tazbid wal Qirat'),
]

SUBJECT_LIST = {
    'takmil':['bukhari 1','bukhari 2','muslim 1','muslim 2','tirmizi 1','tirmizi 2','abu daud','nasai & ibne majah','tahabi','muattan'],
    'fazilat':['meshkat 1','meshkat 2','bayjabi','hedaya 3','hedaya 4','sharhul akaid','nukhbah','tahrik'],
    'sanabia':['mukhtasar','nurul anwar','makamat','tarzama','sharhe bekaya','siraji','insha'],
    'mutawassitah':['nahbemir','panjeganj','rawja','sharhe miat','malabudda','seerat','bangla 7'],
    'ibtedaiyah':['najira','urduki tesri','bangla 5','gonit','talimul islam 4','farsi','somaj biggan'],
    'hifz':['hifz','tajbid','diniyat'],
    'tazbid':['hadar','hifj','tajbid','tartil'],
}


class StudentManager(models.Manager):
    def with_result(self):
        students_with_result = self.filter(result__isnull=False)
        return students_with_result

    def without_result(self):
        students_with_result = self.filter(result__isnull=True)
        return students_with_result


class Student(models.Model):
    name          = models.CharField(max_length=100)
    father        = models.CharField(max_length=100)
    address       = models.CharField(max_length=255,
                                     null=True,
                                     blank=True,
                                     help_text='permanent address of student')

    madrasa       = models.ForeignKey(Madrasa, on_delete=models.CASCADE, related_name='students')
    markaz        = models.CharField(max_length=127,
                                     blank=True,
                                     help_text="If the student's madrasa is the markaz then leave it blank'"
                                               " otherwise enter the markaz name")
    marhala       = models.CharField(max_length=10,
                                     choices=MARHALA)

    reg_year      = models.CharField(max_length=4,
                                     choices=REGISTRATION_YEARS,
                                     default='2018')
    registrar     = models.ForeignKey('auth.User', default=1)
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    is_active    = models.BooleanField(default=True, help_text='Active by Default')

    objects       = StudentManager()


    def get_absolute_url(self):
        return reverse('student:student_detail', kwargs={'pk':self.pk})

    def get_subject_list(self):
        subject_list = SUBJECT_LIST[self.marhala]
        return subject_list

    def get_result(self):
        try:
            return self.result
        except:
            return None

    def __str__(self):
        return '{}, (id: {})'.format(self.name, self.id)

    def save(self, *args, **kwargs):
        if self.markaz:
            return super(Student, self).save(*args, **kwargs)

        if self.madrasa.is_markaz:
            self.markaz = self.madrasa.name
        return super(Student, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-registered_at','-updated_at']
