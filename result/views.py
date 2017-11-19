from collections import OrderedDict
from django.shortcuts import render, reverse, redirect, get_object_or_404

from student.models import Student
from madrasa.models import Madrasa
from result.models import Result
from result.forms import SearchResultForm, ResultFilterForm


def result_search(request):
    total_madrasa = Madrasa.objects.all().count()
    total_student = Student.objects.all().count()

    form = SearchResultForm(request.POST or None)
    id = request.GET.get('id')
    if id:
        return redirect(reverse('result:result_detail', kwargs={'id': int(id)}))

    context = {
        'form': form,
        'total_madrasa': total_madrasa,
        'total_student': total_student,
    }
    return render(request, 'result/result_search.html', context)


def result_detail(request, id=None):
    result = get_object_or_404(Result, student__id=id)
    student = result.student

    result_dict = OrderedDict()
    for i, subject in enumerate(student.get_subject_list(), 1):
        result_dict[subject] = getattr(result, 'subject_{}'.format(i), 0)

    context = {
        'student': student,
        'result': result_dict,
    }
    return render(request, 'result/result_detail.html', context)


def top_results(request):
    results = Result.objects.all().order_by('-average_num', '-total_num')

    # try to find marhala and madrasa on get method
    # then filter results based on madrasa or marhala
    marhala = request.GET.get('marhala')
    if request.GET.get('marhala'):
        results = results.filter(student__marhala__icontains=marhala)

    madrasa = request.GET.get('madrasa')
    if request.GET.get('madrasa'):
        try:
            madrasa = int(madrasa)
            results = results.filter(student__madrasa__id=madrasa)
        except:
            results = results.filter(student__madrasa__name__icontains=madrasa)

    reg_year = request.GET.get('reg_year', 2018)
    results = results.filter(student__reg_year=int(reg_year))

    result_filter_form = ResultFilterForm(request.GET or None)
    context = {
        'result_filter_form': result_filter_form,
        'results': results[:40],
    }
    return render(request, 'result/top_results.html', context)
