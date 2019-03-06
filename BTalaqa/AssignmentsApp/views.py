from django.shortcuts import render
from AssignmentsApp.forms.forms import AssignmentsForm
# Create your views here.


def assign_users(request):
    """
    render html to assign users to test
    :param request:
    :return:
    """
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AssignmentsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            assignment_form = form.save()
            return render(request, 'assignments/assign-users-tests.html',
                          {'form': form})
        else:
            return render(request, 'assignments/assign-users-tests.html',
                          {'form': form})

    else:
        form = AssignmentsForm()
        return render(request, 'assignments/assign-users-tests.html',
                      {'form': form})
