import sys
import pandas as pd

from src.exception import CustomException
from src.utilis import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        pass


class CustomData:

    def __init__( self,
            gender: str,
            race_ethnicity: str,
            parental_level_of_education,
            lunch: str,
            test_preparation_course: str,
            reading_score: str,
            writing_score: str,):

        self.gender = gender
        self.race_ethinicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.race_ethinicity = race_ethnicity
        self.writing_score = writing_score

        

