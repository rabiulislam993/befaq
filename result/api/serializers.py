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
        fields = ['reg_id','reg_year','name','father','marhala','madrasa','result']

    def get_madrasa(self, obj):
        return obj.madrasa.name

    def get_result(self, obj):
        reg_id = obj.reg_id
        reg_year = obj.reg_year
        subject_list = obj.get_subject_list()

        result = Result.objects.get(student__reg_id=reg_id, student__reg_year=reg_year)

        formated_result_dict = OrderedDict()
        for i, subject in enumerate(subject_list, 1):
            formated_result_dict[subject]= getattr(result, 'subject_{}'.format(i), 0)

        formated_result_dict['total']= obj.result.total_num
        formated_result_dict['average']= obj.result.average_num

        return formated_result_dict


#
# class CustomerHyperlink(HyperlinkedRelatedField):
#     # We define these as class attributes, so we don't need to pass them as arguments.
#     # view_name = 'ResultDetialAPIView'
#     view_name = 'api:result_long_url'
#     queryset = Student.objects.all()
#
#     def get_url(self, obj, view_name, request, format):
#         url_kwargs = {
#             'reg_year': obj.reg_year,
#             'reg_id': obj.reg_id
#         }
#         return reverse(view_name, kwargs=url_kwargs, request=request, format=format)



class TopStudentResultsSerializer(ModelSerializer):
    madrasa = SerializerMethodField()
    total_num = SerializerMethodField()
    average_num = SerializerMethodField()
    # results = HyperlinkedRelatedField(view_name='ResultDetialAPIView', read_only=True )

    class Meta:
        model = Student
        fields = ['reg_id', 'reg_year', 'name','madrasa','marhala','total_num','average_num' ]

    def get_madrasa(self, obj):
        return obj.madrasa.name

    def get_total_num(self, obj):
        reg_id = obj.reg_id
        reg_year = obj.reg_year
        result = Result.objects.get(student__reg_id=reg_id, student__reg_year=reg_year)

        return result.total_num

    def get_average_num(self, obj):
        reg_id = obj.reg_id
        reg_year = obj.reg_year
        result = Result.objects.get(student__reg_id=reg_id, student__reg_year=reg_year)

        return result.average_num
