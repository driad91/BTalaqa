import pandas as pd
from MCQAssignmentsApp.models import TestUserAssignment,UnlockedVideo


def get_count_assigned_tests(student):

    """
    Method retrieves number of assigned tests to students completed, and number
    of assigned tests not completed.
    :param student: student user
    :return: the number of completed assigned tests, and the number of
    uncompleted assigned tests
    """
    assigned_tests = \
        TestUserAssignment.objects.filter(user=student).values\
            ('test','assignment_completed')
    count_assigned_uncompleted = assigned_tests.filter\
        (assignment_completed=False).count()
    count_assigned_completed = assigned_tests.filter\
        (assignment_completed=True).count()
    return count_assigned_completed, count_assigned_uncompleted


def get_count_unlocked_videos(student):

    """
    Method retrieves the count of videos unlocked by a specific student
    :param student: student currently logged in
    :return: count of unlocked tests by this specific student
    """

    unlocked_videos = UnlockedVideo.objects.filter(student=student).values()
    return unlocked_videos.count()


