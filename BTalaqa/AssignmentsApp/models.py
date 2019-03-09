from django.db import models
from MCQAssignmentsApp.models import Test
from django.contrib.auth.models import User

# Create your models here.
class Assignments(models.Model):
    """
    Model stores assignments as a combination of user_id and test_id, the idea
    is that teachers assign tests to students in a many to many relationship
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_id', 'test_id')
