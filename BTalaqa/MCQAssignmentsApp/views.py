from django.shortcuts import render, redirect
from MCQAssignmentsApp.forms.forms import TestForm, QuestionForm, AnswerForm, DeleteQuestion, AssignmentsForm
from MCQAssignmentsApp.models import Test, Question, Answer, StudentTestAnswers, TestUserAssignment
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.http import JsonResponse
from django.forms import formset_factory

from MCQAssignmentsApp.helpers import test_helper
import json

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

    try:
        test = Test.objects.get(pk=pk)
        questions = Question.objects.filter(test=test)

    except ObjectDoesNotExist:
        messages.info(request, "There is no test with this id")
        test = None
        questions = []

    answer_form_set = formset_factory(form=AnswerForm,
                                      extra=1,
                                      can_delete=False)

    if request.method == "POST":
        question_form = QuestionForm(request.POST)
        answer_forms = answer_form_set(request.POST)

        if question_form.is_valid():
            valid = True
            question = question_form.save()

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
                messages.info(request, "Question {} created".format(len(questions)))
                # go to the next answer
                return redirect('MCQAssignmentsApp:create_question_answers',
                                pk=pk)
            else:
                messages.warning(request, "One of the forms is not valid")

    return render(request, 'teachers/questions-answers-creation.html',
                  {'question_form': QuestionForm,
                   'answer_formset': answer_form_set,
                   'test': test,
                   'questions': questions
                   })


@login_required
@permission_required('MCQAssignmentsApp.edit_question')
def test_overview(request, pk):
    """
    The overview of all test questions and answers.

    :param request:
    :param pk: primary key of the test
    :return:
    """

    try:
        test = Test.objects.get(pk=pk)
        questions = Question.objects.filter(test=test)

    except ObjectDoesNotExist:
        messages.info(request, "There is no test with this id")
        test = None
        questions = []

    return render(request, 'teachers/test-overview.html',
                  {'test': test,
                   'questions': questions
                   })


@login_required
@permission_required('MCQAssignmentsApp.edit_question')
def delete_question(request, pk, question_pk):
    """
    The view deletes question and all its answers

    :param request:
    :param pk: test pk
    :param question_pk: primary key of the question
    :return:
    """

    try:
        question = Question.objects.get(pk=question_pk)
        answers = Answer.objects.filter(question=question)

    except ObjectDoesNotExist:
        messages.info(request, "There is no question with this id")
        question = None
        answers = []

    if request.method == "POST":
        question_form = DeleteQuestion(request.POST)
        if question_form.is_valid():
            if question_form.cleaned_data["yes_no"]:
                # deleting the question
                question.delete()
                for answer in answers:
                    answer.delete()

                messages.warning(request, "Question was deleted =(")
                return redirect('MCQAssignmentsApp:test_overview',
                                pk=pk)

    return render(request, 'teachers/delete_question.html',
                  {'question': question,
                   'test': Test.objects.get(pk=pk),
                   'answers': answers,
                   'form': DeleteQuestion
                   })


@login_required
def dashboard(request):
    """
    Display statistic about student progress in their tests.

    :param request:
    :return:
    """
    return render(request, 'dashboard.html', {'tests': Test.objects.all()})


@login_required
@permission_required('MCQAssignmentsApp.read_test')
def students_assignments(request):
    """
    returns view of all tests assigned to the logged in student and renders the
    template
    :param request: http request
    :return: template
    """

    user_tests = TestUserAssignment.objects.filter(user__username=request.user)\
        .values('test_id','test_id__name')
    return render(request, 'students/students-assigned-tests.html',
                  context={'user_tests': user_tests})
@login_required
@permission_required('MCQAssignmentsApp.read_test')
def render_test(request, id):
    """
    renders any chosen test by the user in the form of a test
    :param request: http request
    :param id: id of the test to be rendered
    :return:
    """
    relevant_questions = Question.objects.filter(test=id)
    relevant_answers =Answer.objects.filter(question__in=relevant_questions.values_list('id', flat=True))
    return render(request, 'students/selected-test.html', context={'questions': relevant_questions.values(),
                                                                   'answers': relevant_answers.values(),
                                                                   'test_id': id})
@login_required
@permission_required('MCQAssignmentsApp.read_test')
def submit_test(request):
    """
    Handles different things to be done when student submits test, i.e. saving
    of the students answers, removing test as an assignment to this student
    and checks if the answers for this test were already in the database,
    and if so deletes them and updates them with the new values
    :param request: Ajax request
    :return: Msg, containing the score of the student
    """
    data = json.loads(request.POST.get('values'))
    student_answers_dict = data['student_answers']
    student = request.user
    test_id = data['test_id']
    test = Test.objects.get(pk=test_id)
    correct_answers = Answer.objects.filter(is_correct=True,
                                            question__test=test).values('id', 'question_id')
    qs_assignment = TestUserAssignment.objects.filter(test=test, user=student)
    if qs_assignment.exists():
        qs_assignment.delete()
    qs = StudentTestAnswers.objects.filter(test=test, student=student)
    if qs.exists():  # if student has previous answers for this test
        qs.delete()  # delete
    for k, v in student_answers_dict.items():
        question = Question.objects.get(pk=k)  # retrieving question item from id
        answer = Answer.objects.get(pk=v)  # retrieving answer obj from id
        test_answer = StudentTestAnswers.objects.create(student=student,
                                                        question=question,
                                                        answer=answer,
                                                        test=test)
        test_answer.save()
    percentage, corrections_dict = test_helper.test_correction\
        (student_answers=student_answers_dict, model_answers=correct_answers)
    return JsonResponse({'percentage': percentage*100,
                         'corrections_dict': corrections_dict})

def assign_users(request):
    """
    render html to assign users to test
    :param request:
    :return:
    """
    assignments_all_existing = TestUserAssignment.objects.all()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AssignmentsForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            assignment_form = form.save()
            assignments_all_existing = TestUserAssignment.objects.all()
            return render(request, 'teachers/assign-users-tests.html',
                          {'form': form, 'existing_assignments': assignments_all_existing})
        else:
            return render(request, 'teachers/assign-users-tests.html',
                          {'form': form, 'existing_assignments': assignments_all_existing})

    else:
        form = AssignmentsForm()
        return render(request, 'teachers/assign-users-tests.html',
                      {'form': form, 'existing_assignments': assignments_all_existing})
