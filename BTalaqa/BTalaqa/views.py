from django.shortcuts import render, reverse
# Create your views here.
# generic project views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect



@login_required
def about(request):
    """
    home view of the project

    :param request:
    :return:
    """
    # TODO shall this code be moved to one of the apps?

    return render(request, 'common/about.html', context={})

@login_required
def home(request):
    qs = Group.objects.filter(user=request.user).values_list('name',flat=True)
    print(qs)
    if 'Students' in qs:
        return HttpResponseRedirect(reverse('MCQAssignmentsApp:students_home'))
    else:
        return HttpResponseRedirect(reverse('MCQAssignmentsApp:teachers_home'))

