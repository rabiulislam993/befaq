from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
# class APIDocAPIView(APIView):
#     def get(self, request):
#         doc_dict = {
#             'API URL':'www.befaq.ml/api/result/  for single result, '
#                       'www.befaq.ml/api/result/top/ for top results list,',
#
#             'retrieve single result from get request': 'to retrieve a student result make a get request to '
#                                                        'www.befaq.ml/api/result/ with tow arguments '
#                                                        '1) reg_id , send student registration ID in reg_id argument '
#                                                        '2) reg_year, send student registration Year in reg_year argument',
#
#             'retrieve single result from flat URL': 'to retrieve a student result make a get request to '
#                                                     'www.befaq.ml/api/result/<reg_year>/<reg_id>/ where reg_year is '
#                                                     'student registration year and reg_id is student registration ID '
#                                                     'example: go to www.befaq.ml/api/result/2017/2/ for retrieve result of '
#                                                     'student whose registration ID is 2 and registration year is 2017',
#
#             'retrieve top results list': 'top result',
#         }
#
#         return Response(doc_dict)

class APIDoc(TemplateView):
    template_name = 'api/api_doc.html'
