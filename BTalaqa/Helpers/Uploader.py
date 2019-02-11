import pandas as pd

class Uploader:
    """
    Uploader class to handle the quesitons and answers given as files and
    enter them in the database.
    """
    as_test = None
    questions = pd.DataFrame()
    answers = pd.DataFrame()

