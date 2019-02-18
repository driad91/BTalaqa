import pandas as pd
from . import Check

class Uploader:
    """
    Uploader class to handle the quesitons and answers given as files and
    enter them in the database.
    """

    def __init__(self, as_test=False, questions = pd.DataFrame()
                 , answers= pd.DataFrame()):
        """
        Constructor

        :param as_test:
        :param questions:
        :param answers:
        """
        self.as_test = as_test
        self.questions = questions
        self.answers = answers

    def upload_questions(self):
        """

        :return:
        """