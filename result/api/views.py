from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_406_NOT_ACCEPTABLE
from rest_framework.generics import RetrieveAPIView, ListAPIView

from result.api.serializers import StudentResultSerializer, TopStudentResultsSerializer
from student.models import Student


@api_view(['get'])
def api_home(self):
    content = {'single_result':'To retrieve single result Go to www.befaq.ml/api/result/<id>/ where <id> is student registration ID',
               'result_list':'To retrieve top result list Go to www.befaq.ml/api/result/top/',
               'detail':'Learn Detail on www.befaq.ml/api/'}
    return Response(content, HTTP_406_NOT_ACCEPTABLE)


class ResultDetailAPIView(RetrieveAPIView):
    serializer_class = StudentResultSerializer
    queryset = Student.objects.all()
    lookup_field = 'id'

class TopStudentResultsAPIView(ListAPIView):
    serializer_class = TopStudentResultsSerializer

    def get_queryset(self):
        # retrieve all student object with result
        queryset = Student.objects.with_result()

        # filter student objects with get parameters if given.
        # first filter them with reg_year, default 2018
        reg_year = self.request.GET.get('reg_year', 2018)
        queryset = queryset.filter(reg_year=int(reg_year))

        # filter them with marhala if given
        marhala = self.request.GET.get('marhala')
        if marhala:
            queryset = queryset.filter(marhala__icontains=marhala)

        # filter them with madrasa if givem
        madrasa = self.request.GET.get('madrasa')
        if madrasa:
            try: # try to find if the given 'madrasa' parameter is int type (for madrasa ID)
                madrasa = int(madrasa) # convert madrasa id to integer type
                queryset = queryset.filter(madrasa__id=madrasa)
            except: # if madrasa not an int, then think of his as string (madrasa name)
                queryset = queryset.filter(madrasa__name=madrasa)

        return queryset