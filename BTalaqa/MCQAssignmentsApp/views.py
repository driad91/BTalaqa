from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render

from MCQAssignmentsApp.forms.forms import TestForm, question_form_set

def create_test(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            test_object = form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/quesitons_answers/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestForm()

    return render(request, 'test-creation.html', {'form': form})

def create_questions_answers(request):
    """

    :param request:
    :return:
    """
    formset = question_form_set
    return render(request, 'questions-answers-creation.html', {'formset': formset})

