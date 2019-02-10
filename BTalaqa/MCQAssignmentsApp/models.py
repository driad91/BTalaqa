from django.db import models

# Create your models here.


class Question(models.Model):
    """
    Model stores MCQ Questions
    """
    text = models.CharField(max_length=255)
    exclusive_answer = models.BooleanField(default=True)


class Answer(models.Model):
    """
    Model stores MCQ Answers to be displayed per question
    """
    text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class ModelAnswers(models.Model):
    """
    Model stores model answers to questions by containing references
    to questions and answers, model made initially to store possibly multiple
    correct answers per questions in case that is needed in the future.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


class Test(models.Model):
    """
    Model stores tests as in each test includes a combination of possible
    questions to be able to create different tests as different combinations
    of different already existing questions
    """
    name = models.CharField(max_length=255)


class TestQuestions(models.Model):
    """
    Model stores the references to each test and the questions it contains
    """
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)







