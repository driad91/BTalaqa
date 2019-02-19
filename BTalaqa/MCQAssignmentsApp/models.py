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
    is_correct = models.BooleanField(default=False)

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







