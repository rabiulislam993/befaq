from collections import OrderedDict

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, reverse, redirect, get_object_or_404

from student.models import Student
from madrasa.models import Madrasa
from .models import Result
from .forms import SearchResultForm, ResultFilterForm, AddResultForm


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


@login_required
def select_student_to_add_result(request):
    context = {}  # initialize context
    if request.method == 'POST':
        form = SearchResultForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get('id')
            context['student_id'] = id
            # checking if the student of given id already exists or not
            student = Student.objects.filter(id=id)
            if student.exists():
                # checking if the student's result already exists or not
                result_exists = Result.objects.filter(student__id=id).exists()
                if result_exists:
                    # if result already exists then send this information as error
                    context['result_exists'] = True
                # if student of given id is exists and his result not exists
                # then go to add result page for adding new result for this student
                else:
                    return redirect(reverse('result:add_result', kwargs={'id': id}))
            else:  # if student not exists then send this information
                context['student_not_exists'] = True
    else:
        form = SearchResultForm()

    context['form'] = form
    return render(request, 'result/select_student_to_add_result.html', context)


@login_required
def add_result(request, id):
    student = get_object_or_404(Student, id=id)
    # if this student already have result then raise 404 error
    result_exists = Result.objects.filter(student__id=id).exists()
    if result_exists:
        raise Http404

    subject_list = student.get_subject_list()

    add_result_form = AddResultForm(request.POST or None, subject_list=subject_list)
    if add_result_form.is_valid():
        subject_result_dict = add_result_form.get_results()
        # if all results is valid then create new result object
        # and add current student to this result.
        Result.objects.create(student=student, **subject_result_dict)
        messages.success(request, 'Result for Student ID: {} Successfully Added'.format(student.id))
        # after successfully create result, return to student's result page
        # or to new result add page, if submitted 'save and add new result' button
        if 'add_another' in request.POST:
            return redirect('result:select_student_to_add_result')
        return redirect(reverse('result:result_detail', kwargs={'id': student.id}))

    context = {'add_result_form': add_result_form,
               'student': student,
               }
    return render(request, 'result/add_result.html', context)


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
    filter_info = []  # show filter information as message on top results page
    marhala = request.GET.get('marhala')
    if request.GET.get('marhala'):
        results = results.filter(student__marhala__icontains=marhala)
        filter_info.append('Marhala: {}'.format(marhala))  # include marhala into filter info

    madrasa = request.GET.get('madrasa')
    if request.GET.get('madrasa'):
        try:
            madrasa_id = int(madrasa)
            results = results.filter(student__madrasa__id=madrasa_id)
            filter_info.append('Madrasa ID: {}'.format(madrasa_id))  # include madrasa id into filter info
        except:
            results = results.filter(student__madrasa__name__icontains=madrasa)
            filter_info.append('Madrasa: {}'.format(madrasa))  # include madrasa name into filter info

    reg_year = request.GET.get('reg_year', 2018)
    results = results.filter(student__reg_year=int(reg_year))
    filter_info.append('Year: {}'.format(reg_year))  # include registration Year into filter info

    # convert filter_info list to comma separated String
    filter_info = ', '.join(filter_info)

    result_filter_form = ResultFilterForm(request.GET or None)
    context = {
        'result_filter_form': result_filter_form,
        'filter_info': filter_info,
        'results': results[:40],  # always return top 40 results
    }
    return render(request, 'result/top_results.html', context)
