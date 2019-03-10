from django.shortcuts import render

# Create your views here.
# generic project views
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    """
    home view of the project

    :param request:
    :return:
    """
    # TODO shall this code be moved to one of the apps?

    return render(request, 'common/home.html', context={})
