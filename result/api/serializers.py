from collections import OrderedDict
from rest_framework.serializers import (Serializer,
                                        ModelSerializer,
                                        SerializerMethodField,
                                        HyperlinkedRelatedField)
from rest_framework.reverse import reverse

from result.models import Result
from student.models import Student


class StudentResultSerializer(ModelSerializer):
    madrasa = SerializerMethodField()
    result = SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id','reg_year','name','father','address','marhala','madrasa','markaz','result']

    def get_madrasa(self, obj):
        return obj.madrasa.name

    def get_result(self, obj):
        subject_list = obj.get_subject_list()
        reg_id = obj.id
        reg_year = obj.reg_year

        result = Result.objects.get(student__id=reg_id, student__reg_year=reg_year)

        formated_result_dict = OrderedDict()
        for i, subject in enumerate(subject_list, 1):
            formated_result_dict[subject]= getattr(result, 'subject_{}'.format(i), 0)

        formated_result_dict['total']= obj.result.total_num
        formated_result_dict['average']= obj.result.average_num
        formated_result_dict['grade']= obj.result.grade

        return formated_result_dict


class TopStudentResultsSerializer(ModelSerializer):
    madrasa = SerializerMethodField()
    total_num = SerializerMethodField()
    average_num = SerializerMethodField()
    # results = HyperlinkedRelatedField(view_name='ResultDetialAPIView', read_only=True )

    class Meta:
        model = Student
        fields = ['id', 'reg_year', 'name','madrasa','marhala','total_num','average_num' ]

    def get_madrasa(self, obj):
        return obj.madrasa.name

    def get_total_num(self, obj):
        id = obj.id
        reg_year = obj.reg_year
        result = Result.objects.get(student__id=id, student__reg_year=reg_year)
        return result.total_num

    def get_average_num(self, obj):
        id = obj.id
        reg_year = obj.reg_year
        result = Result.objects.get(student__id=id, student__reg_year=reg_year)
        return result.average_num