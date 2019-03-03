from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from MCQAssignmentsApp.forms.forms import TestForm, answer_form_set,QuestionForm,AnswerForm
from django.contrib.auth.decorators import login_required



@login_required
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
            print(test_object.id)
            return HttpResponseRedirect('/questions_answers/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestForm()

    return render(request, 'test-creation.html', {'form': form})

@login_required
def create_questions_answers(request):
    """

    :param request:
    :return:
    """
    #formset = questio n_form_set

    if request.method == "POST":
        question_form = QuestionForm(request.POST)
        answer_forms = answer_form_set(request.POST)

        if question_form.is_valid():
            question = question_form.save()
            for answer_form in answer_forms:
                if answer_form.is_valid():
                    answer_form = answer_form.save(commit=False)
                    answer_form.question=question
                    answer_form.save()
                    #return whatever!!!



    else:
        return render(request, 'questions-answers-creation.html'
                  , {'question_form': QuestionForm, 'answer_formset': answer_form_set})

@login_required
def home (request):
    return render(request,'home.html')
