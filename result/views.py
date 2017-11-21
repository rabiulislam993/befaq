from collections import OrderedDict
from django.shortcuts import render, reverse, redirect, get_object_or_404

from student.models import Student
from madrasa.models import Madrasa
from result.models import Result
from result.forms import SearchResultForm, ResultFilterForm


def result_search(request):
    total_madrasa = Madrasa.objects.all().count()
    total_student = Student.objects.all().count()

    if request.method == 'POST':
        form = SearchResultForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get('id')
            return redirect(reverse('result:result_detail', kwargs={'id': id}))

    else:
        form = SearchResultForm()

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
    filter_info = [] # show filter information as message on top results page
    marhala = request.GET.get('marhala')
    if request.GET.get('marhala'):
        results = results.filter(student__marhala__icontains=marhala)
        filter_info.append('Marhala: {}'.format(marhala)) # include marhala into filter info

    madrasa = request.GET.get('madrasa')
    if request.GET.get('madrasa'):
        try:
            madrasa_id = int(madrasa)
            results = results.filter(student__madrasa__id=madrasa_id)
            filter_info.append('Madrasa ID: {}'.format(madrasa_id)) # include madrasa id into filter info
        except:
            results = results.filter(student__madrasa__name__icontains=madrasa)
            filter_info.append('Madrasa: {}'.format(madrasa)) # include madrasa name into filter info

    reg_year = request.GET.get('reg_year', 2018)
    results = results.filter(student__reg_year=int(reg_year))
    filter_info.append('Year: {}'.format(reg_year)) # include registration Year into filter info

    # convert filter_info list to comma separated String
    filter_info = ', '.join(filter_info)

    result_filter_form = ResultFilterForm(request.GET or None)
    context = {
        'result_filter_form': result_filter_form,
        'filter_info':filter_info,
        'results': results[:40], # always return top 40 results
    }
    return render(request, 'result/top_results.html', context)
