from django.shortcuts import render

# Create your views here.
# generic project views
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required
def home (request):
    try:
        group = request.user.groups.filter(user=request.user)[0]
        group_name = group.name
    except Exception as E:
        group_name = ''
    if group_name == 'Teachers':
        template_to_extend = 'teachers/base.html'
    else:
        template_to_extend = 'students/base.html'
    return render (request, 'common/home.html', context={'template_to_extend':
                                                             template_to_extend})

