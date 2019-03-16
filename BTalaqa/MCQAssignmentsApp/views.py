from django.shortcuts import render, redirect
from MCQAssignmentsApp.forms.forms import TestForm, answer_form_set, QuestionForm, AnswerForm
from MCQAssignmentsApp.models import Test, Question
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


@login_required
@permission_required('MCQAssignmentsApp.edit_test')
def create_test(request):
    """
    a view to create tests.

    :param request:
    :return:
    """
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            test_object = form.save()
            messages.info(request, "Test created")

            return redirect('MCQAssignmentsApp:create_question_answers', pk=test_object.id)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestForm()

    return render(request, 'teachers/test-creation.html', {'form': form})


@login_required
@permission_required('MCQAssignmentsApp.edit_question')
def create_questions_answers(request, pk):
    """
    The view for teachers to create their questions and answers to them.

    :param request:
    :param pk: primary key of the test
    :return:
    """

    test = None
    if request.method == "POST":
        question_form = QuestionForm(request.POST)
        answer_forms = answer_form_set(request.POST)

        if question_form.is_valid():
            valid = True
            question = question_form.save()

            for answer_form in answer_forms:
                if answer_form.is_valid():
                    name = answer_form.cleaned_data.get('name')
                    if name:
                        print(name)
                    answer_form = answer_form.save(commit=False)
                    answer_form.question = question
                    answer_form.save()
                    test_current = Test.objects.get(pk=pk)
                    question.test.add(test_current)
                else:
                    valid = False
            if valid:
                messages.info(request, "Question {} created".format(question.id))
                # go to the next answer
                return redirect('MCQAssignmentsApp:create_question_answers',
                                pk=pk)
            else:
                messages.warning(request, "One of the forms is not valid")

    else:
        try:
            test = Test.objects.get(pk=pk)
        except ObjectDoesNotExist:
            messages.info(request, "There is no test with this id")

    return render(request, 'teachers/questions-answers-creation.html',
                  {'question_form': QuestionForm,
                   'answer_formset': answer_form_set,
                   'test': test})
