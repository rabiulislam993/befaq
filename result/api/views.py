from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST

from result.api.serializers import StudentResultSerializer, TopStudentResultsSerializer
from result.models import Result
from student.models import Student


class ResultDetailAPIView(APIView):
    def get(self, request, reg_year=None, reg_id=None,  format=None):
        # first check if reg_id and reg_year provided by get method
        # if not provided then try to grab from url
        reg_year = request.GET.get('reg_year', reg_year)
        reg_id = request.GET.get('reg_id', reg_id)

        # if reg_id and reg_year not provided on get method or in url
        # then return bad request error
        if not reg_id or not reg_year:
            return Response({'error':'Registration ID or registration Year Missing. '
                                     'Go to www.befaq.ml/api for API documentation.'}, HTTP_400_BAD_REQUEST)

        # if reg_id and reg_year provided then try to find relative result
        # from Student class, if not found then return 404 not found error
        try:
            result = Student.objects.get(reg_id=reg_id, reg_year=reg_year)
        except:
            return Response({'error':'result not found'}, HTTP_404_NOT_FOUND)

        # serialize grabbed data and return as api Response
        result = StudentResultSerializer(result)
        return Response(result.data)

class TopStudentResultsAPIView(APIView):
    def get(self, request, format=None):
        student_results = Student.objects.exclude(result__isnull=True).order_by('-result__average_num', '-result__total_num')

        # try to find marhala and madrasa on get method
        # then filter results based on madrasa or marhala
        marhala = request.GET.get('marhala')
        if marhala:
            student_results = student_results.filter(marhala__icontains=marhala)

        madrasa = request.GET.get('madrasa')
        if madrasa:
            student_results = student_results.filter(madrasa__name__icontains=madrasa)

        serialized_results = TopStudentResultsSerializer(student_results, many=True)

        return Response(serialized_results.data)
