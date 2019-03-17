from django.db import models
from django.contrib.auth.models import User


class Test(models.Model):
    """
    Model stores tests as in each test includes a combination of possible
    questions to be able to create different tests as different combinations
    of different already existing questions
    """
    name = models.CharField(max_length=255, blank=False)
    assignment = models.ManyToManyField('auth.User', through='TestUserAssignment', related_name='assignment')

    class Meta:
        app_label = 'MCQAssignmentsApp'
        permissions = (
            ("edit_test", "Can edit test"),
            ("read_test", "Can read test"),
        )
        verbose_name = 'test'
        verbose_name_plural = 'tests'

    def __str__(self):
        return '%s %s' % (self.id, self.name)


class Question(models.Model):
    """
    Model stores MCQ Questions
    """
    text = models.CharField(max_length=255, blank=False, null=False)
    exclusive_answer = models.BooleanField(default=True)
    test = models.ManyToManyField(Test)

    class Meta:
        app_label = 'MCQAssignmentsApp'
        permissions = (
            ("edit_question", "Can edit question"),
            ("read_question", "Can read question"),
        )
        verbose_name = 'question'
        verbose_name_plural = 'questions'


class Answer(models.Model):
    """
    Model stores MCQ Answers to be displayed per question
    """
    text = models.CharField(max_length=255, blank=False, null=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    class Meta:
        app_label = 'MCQAssignmentsApp'
        permissions = (
            ("edit_answer", "Can edit answer"),
            ("read_answer", "Can read answer"),
        )
        verbose_name = 'answer'
        verbose_name_plural = 'answers'


class StudentTestAnswers (models.Model):
    """
    Model Stores the students answers to tests
    """
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey (Test, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    class Meta:
        app_label = 'MCQAssignmentsApp'
        verbose_name = 'student answer'
        verbose_name_plural = 'student answers'
        unique_together = ('student', 'test', 'question','answer')


class TestUserAssignment(models.Model):

    """
    Model stores assignments as a combination of user_id and test_id, the idea
    is that teachers assign tests to students in a many to many relationship
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    #teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher')

    class Meta:

        app_label = 'MCQAssignmentsApp'
        unique_together = ('user', 'test')
        permissions = (
            ("edit_assignment", "Can edit assignment"),
            ("read_assignment", "Can read assignment"),
        )
        verbose_name = 'user_test'
        verbose_name_plural = 'user_tests'
