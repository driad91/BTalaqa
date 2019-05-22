import pandas as pd
from MCQAssignmentsApp.models import Test, Answer, StudentTestAnswers, TestUserAssignment


def test_correction(student_answers, model_answers):
    """
    Method corrects test, given answers given by student, and model_answers

    :param student_answers: dictionary of answers given by students
    :param model_answers: QuerySet of containing questions from a test, and each question's model answer(s)
    :return: score as a decimal percentage, corrections_dictionary which is a dictionary containing as key the question's id and as value a tuple containing the student's answer as the first element and model answer(s) as a list
    """

    df_model_answers = pd.DataFrame(list(model_answers))
    corrections_dict = {}
    correct_answers = 0
    for k, v in student_answers.items():
        answers = df_model_answers[df_model_answers['question_id'] == int(k)]['id']
        if not answers.empty:
            corrections_dict[int(k)] = int(v), list(answers)
            if int(v) in answers.unique():
                correct_answers += 1
    score = correct_answers/len(student_answers)
    return score, corrections_dict


def calculate_test_score_only(student_answers, model_answers):
    """
    TODO

    :param student_answers:
    :param model_answers:
    :return:
    """
    correct_answers = 0
    for question in student_answers['question_id']:
        student_answer_to_question = \
            student_answers[student_answers['question_id'] == question]
        model_answers_to_question = model_answers[model_answers['question_id'] == question]
        if not model_answers_to_question.empty:
            if student_answer_to_question['answer_id'].iloc[0]\
                    in model_answers_to_question['id'].unique():
                correct_answers += 1
    return correct_answers/student_answers.shape[0]


def test_scores_by_student(student):
    """
    Method to calculate the score of a specific student in all tests taken from
    database.

    :param student: user_id of student logged in
    :return: Dictionary where key is the test and value is the score
    """
    student_test_answers_qs = \
        StudentTestAnswers.objects.filter(student=student).values()
    if not student_test_answers_qs:
        return dict(), False
    student_test_answers_df = pd.DataFrame(list(student_test_answers_qs))

    test_scores = {}
    dashboard_scores = {"assigned_tests": [],
                        "additional_tests": [],
                        "all_tests": [],
                        "number_of_completed_assigned_tests": 0,
                        "number_of_completed_additional_tests": 0
                        }

    assigned_tests_ids = TestUserAssignment.objects.filter(user=student)\
        .values_list('test__id', flat=True)

    all_tests = Test.objects.all()
    tests_done_by_student = list(student_test_answers_df['test_id'].unique())

    for current_test in all_tests:

        # check if test in
        if current_test.id in tests_done_by_student:

            correct_answers = pd.DataFrame(list(Answer.objects.filter(is_correct=True,
                                                                      question__test=current_test).values('id',
                                                                                                          'question_id')))
            student_test_answers = student_test_answers_df[student_test_answers_df['test_id'] == current_test.id]

            score = calculate_test_score_only(student_answers=student_test_answers,
                                              model_answers=correct_answers)

            test_scores[current_test] = str(int(score*100)) + '%'

            if current_test.id in assigned_tests_ids:
                dashboard_scores["number_of_completed_assigned_tests"] += 1
                dashboard_scores["assigned_tests"].append(score)
            else:
                dashboard_scores["number_of_completed_additional_tests"] += 1
                dashboard_scores["additional_tests"].append(score)
            dashboard_scores["all_tests"].append(score)
    try:
        dashboard_scores["assigned_tests"] = str(int(pd.np.mean(dashboard_scores["assigned_tests"]) * 100)) + '%'
    except ValueError:
        dashboard_scores["assigned_tests"] = "0%"
    try:
        dashboard_scores["additional_tests"] = str(int(pd.np.mean(dashboard_scores["additional_tests"]) * 100)) + '%'
    except ValueError:
        dashboard_scores["additional_tests"] = "0%"
    try:
        dashboard_scores["all_tests"] = str(int(pd.np.mean(dashboard_scores["all_tests"]) * 100)) + '%'
    except ValueError:
        dashboard_scores["all_tests"] = "0%"
    dashboard_scores["count_assigned_tests"] = len(assigned_tests_ids)
    return test_scores, dashboard_scores
