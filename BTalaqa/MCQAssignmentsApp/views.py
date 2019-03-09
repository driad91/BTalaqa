from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render,reverse, redirect
from MCQAssignmentsApp.forms.forms import TestForm, answer_form_set,QuestionForm,AnswerForm
from MCQAssignmentsApp.models import Test,Question
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
            return redirect('MCQAssignmentsApp:create_question_answers',pk= test_object.id)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestForm()

    return render(request, 'teachers/test-creation.html', {'form': form})

@login_required
def create_questions_answers(request, pk):
    """

    :param request:
    :return:
    """
    #formset = question_form_set

    if request.method == "POST":
        question_form = QuestionForm(request.POST)
        answer_forms = answer_form_set(request.POST)

        if question_form.is_valid():
            valid = True
            question = question_form.save()
            print("HERE QUESTION")
            print(question.pk)
            for answer_form in answer_forms:
                if answer_form.is_valid():
                    answer_form = answer_form.save(commit=False)
                    answer_form.question = question
                    answer_form.save()
                    test_current = Test.objects.get(pk=pk)
                    question.test.add(test_current)
                else:
                    valid = False
            if valid:
                return redirect('MCQAssignmentsApp:create_question_answers',
                                pk=pk)


    else:

        test = Test.objects.get(pk=pk)
        return render(request, 'teachers/questions-answers-creation.html'
                  , {'question_form': QuestionForm, 'answer_formset': answer_form_set,
                     'test': test})
