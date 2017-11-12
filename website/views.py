from collections import OrderedDict

from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.messages.views import messages

from result.models import Result
from student.models import Student

from result.forms import ResultForm
from student.forms import StudentForm


def home(request):
    return HttpResponse('website home')

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.registrar = request.user
            student.save()
            messages.success(request, 'Name: {}, Id: {} Registered Successfully'.format(student.name, student.reg_id))

            if 'continue' in request.POST:
                messages.info(request, 'register another student')
                form = StudentForm()
            else:
                return redirect(student)

    else:
        form = StudentForm()

    context = {
        'form':form,
    }
    return render(request, 'student/student_form.html', context)

def student_detail(request, reg_id, reg_year):
    student = get_object_or_404(Student, reg_id=reg_id, reg_year=reg_year)
    result = student.get_result()
    result_dict = OrderedDict()
    if result:
        for i, subject in enumerate(student.get_subject_list(), 1):
            result_dict[subject]= getattr(result, 'subject_{}'.format(i), 0)

    context = {
        'student':student,
        'results':result_dict,
    }
    return render(request, 'student/student_detail.html', context)

def student_update(request, reg_id, reg_year):
    student = get_object_or_404(Student, reg_id=reg_id, reg_year=reg_year)
    if request.method == 'POST':
        form = StudentForm(request.POST or None, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.registrar = request.user
            student.save()
            messages.success(request, 'Name: {}, Id: {} Updated Successfully'.format(student.name, student.reg_id))
            return redirect(student)

    else:
        form = StudentForm(instance=student)

    context = {
        'form':form,
    }
    return render(request, 'student/update_form.html', context)


def add_result(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.registrar = request.user
            result.save()
            messages.success(request, 'Result for Student id: {} Successfully added'.format(result.student.reg_id))

            if 'continue' in request.POST:
                messages.info(request, 'add another result')
                form = ResultForm()
            else:
                return redirect(result)

    else:
        form = ResultForm()

    context = {
        'form':form,
    }
    return render(request, 'result/result_form.html', context)


def result_update(request, reg_id, reg_year):
    student = get_object_or_404(Student, reg_id=reg_id, reg_year=reg_year)
    result  = get_object_or_404(Result, student=student)

    if request.method == 'POST':
        form = ResultForm(request.POST or None, instance=result)
        if form.is_valid():
            result = form.save()
            messages.success(request, 'Result for Student id: {} Updated'.format(result.student.reg_id))
            return redirect(result)

    else:
        form = ResultForm(instance=result)

    context = {
        'form':form,
    }
    return render(request, 'result/update_form.html', context)