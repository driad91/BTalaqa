from django.shortcuts import render

# Create your views here.
# generic project views
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required
def check_user_distribute(request):
    """
    Method checks user group and redirects to respective view accordingly,
    either student or teacher.

    :param request:
    :return: correct html view
    """
    try:
        group = request.user.groups.filter(user=request.user)[0]
        group_name = group.name
    except Exception as E:
        group_name = ''

    if group_name == "Students":
        return HttpResponseRedirect(reverse('StudentsApp:home'))
    elif group_name == "Teachers":
        return HttpResponseRedirect(reverse('TeachersApp:home'))
    else:
        return HttpResponseRedirect(reverse('StudentsApp:home'))


