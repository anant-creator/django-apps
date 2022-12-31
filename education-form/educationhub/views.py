from django.shortcuts import render, get_object_or_404
#from django.http import Http404
from .models import all_courses, details
#from django.template import loader

# Create your views here.
def courses(request):
    ac = all_courses.objects.all()
    context = {'ac':ac,}
    return render(request, 'register.html', context)

def detail(request, course_id):
    course = get_object_or_404(all_courses, pk=course_id)
    return render(request, 'details.html', {'course': course, 'ct': details.ct})

def yourchoice(request, course_id):
    course = get_object_or_404(all_courses, pk=course_id)
    try:
        selected_ct = course.details_set.get(pk=request.POST['choice'])
    except (KeyError, all_courses.DoesNotExist):
        return render(request, 'details.html', {'course': course, 'error_message': 'select a valid option'})
    else:
        selected_ct.your_choice = True
        selected_ct.save()
        return render(request, 'details.html', {'course': course})