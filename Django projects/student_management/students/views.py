from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course, Marks
from .forms import StudentForm, CourseForm, MarksForm
from django.db.models import Avg

def home(request):
    return redirect('student_list')

def student_list(request):
    students = Student.objects.all()
    # compute average marks per student
    averages = {s.id: s.marks.aggregate(avg=Avg('marks'))['avg'] or 0 for s in students}
    return render(request, 'students/student_list.html', {'students': students, 'averages': averages})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'students/course_list.html', {'courses': courses})

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'students/course_form.html', {'form': form})

def marks_create(request):
    if request.method == 'POST':
        form = MarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = MarksForm()
    return render(request, 'students/marks_form.html', {'form': form})
