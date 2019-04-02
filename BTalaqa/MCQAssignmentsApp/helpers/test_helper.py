import pandas as pd
from MCQAssignmentsApp.models import Test, Answer, StudentTestAnswers


def test_correction(student_answers, model_answers):

    """
    Method corrects test, given answers given by student, and model_answers
    :param student_answers: dictionary of answers given by students
    :param model_answers: QuerySet of containing questions from a test, and
    each question's model answer(s)
    :return: score as a decimal percentage, corrections_dictionary which is a
    dictionary containing as key the question's id and as value a tuple containing
    the student's answer as the first element and model answer(s) as a list
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
    correct_answers = 0
    for question in student_answers['question_id']:
        student_answer_to_question = \
            student_answers[student_answers['question_id'] == question]
        model_answers_to_question = model_answers[model_answers['question_id'] == question]
        if not model_answers_to_question.empty:
            print("STUDENT ANSWERS")
            print(student_answer_to_question['answer_id'])
            print("MODEL ANSWERS")
            print(model_answers_to_question['id'].unique())
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
    student_test_answers_qs=\
        StudentTestAnswers.objects.filter(student=student).values()
    if not student_test_answers_qs:
        return pd.DataFrame()
    student_test_answers_df = pd.DataFrame(list(student_test_answers_qs))
    test_scores = {}
    for test_id in student_test_answers_df['test_id'].unique():
        current_test = Test.objects.get(pk=test_id)
        correct_answers = pd.DataFrame(list(Answer.objects.filter(is_correct=True,
                                                question__test=current_test).values('id', 'question_id')))
        student_test_answers = student_test_answers_df[student_test_answers_df['test_id'] == test_id]
        score = calculate_test_score_only(student_answers=student_test_answers,
                                  model_answers=correct_answers)
        test_scores[current_test] = str(int(score*100)) + '%'
    return test_scores











