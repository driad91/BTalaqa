import pandas as pd


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

