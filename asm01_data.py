"""
class "Exam_Data" is created with descriptions below:
    The initiated instance of Exam_Data is one DataFrame which was collect from class[1..].txt
    Check_student_code(..) is used to verify the valid code of student
    Check_answer_quantity(...) is used to make sure the 25-answers
    Export the grade score
    Export the analytic values
"""
import pandas as pd
import numpy as np
from asm01_file import *


class ClassGrade:
    def __init__(self, classDf):
        """
        :param classDf: the DataFrame from raw Data. This DataFrame is loaded from File()
        """
        #   initiate the class: Class is converted to DataFrame from the reading of File
        self.classDf = classDf

    def _check_student_code(self):
        """
        Sub module to check the format of student code with below information
        :param
        :return: True if the student Code:
        - Start with N
        - Format as 'N' and 8-digits
        """
        df = self.classDf.copy()
        n = len(df)

        #   Create the processing 'Student Code Check to check the valid Student Code
        #   with default 'valid' value
        analysisCol = ['Valid' for _ in range(n)]
        df.insert(loc=1, column='Valid St. Code', value=np.array(analysisCol))

        #   Loop the DataFrame to check the valid code
        for i in range(n):
            studentCode = df.loc[i, 'Student Code']
            if not (len(studentCode) == 9 and str(studentCode).startswith('N') \
                and studentCode[1:].isdigit()):
                df.loc[i, 'Valid St. Code'] = 'Invalid'

        #   Filter the Invalid data, move to new data frame then refresh the orginal DataFrame
        filtered_dataFrame = df[df['Valid St. Code'] == 'Invalid']

        return filtered_dataFrame

    def _check_answer_quantity(self):
        """
        sub moduel to check the quantity of student's answer
        :param studentAnswer: a row of DataFrame
        :return: True if the data which contains more than 25 answers
        """
        df = self.classDf.copy()
        n = len(df)

        #   Create the processing 'Qty of Answer' column to check the valid Student's answers
        #   Move this column to 2
        analysisCol = ['Valid' for _ in range(n)]
        df.insert(loc=1, column='Qty of Answer', value=np.array(analysisCol))

        #   Loop the DataFrame to check the valid code
        for i in range(n):
            studentAnswer = df.iloc[i, 2:].dropna()
            if len(studentAnswer) != 25:
                df.loc[i, 'Qty of Answer'] = 'Invalid'

        filtered_dataFrame = df[df['Qty of Answer'] == 'Invalid']

        return filtered_dataFrame

    def _clean_data(self, dataFrame):
        """
        Module to clean the surplus data
        :param dataFrame:
        :return: cleaned dataframe
        """
        #   Count the number of columns
        cols = dataFrame.shape[1]
        if cols <= 26:
            return dataFrame
        else:
            df = dataFrame.drop(dataFrame.iloc[:, 26:], axis=1)
            return df

    def _grade_student(self):
        """
        Module for grading the student's answers
        :return: the result of invalid and valid data
        Step 0 - Check validity of data, if the length is more than 26, delete the columns
                return the df0
        Step 1 - Set index of df0 to Student Code, mark all ''-missing answer to zero 0
        Step 2 - Compare answer with df0 and mark down all 'True' answer to DataFrame df1
        Step 3 - Convert all True answer to 4, False Answer to -1 >> DataFrame df2
        Step 4 - Find all position of missing answer '' in df0
        Step 4 - Creat a copy of df2 from df1 with all mark (4) and (-1)
        Step 5 - Fill all zero 0 to new dataframe df2
        Step 6 - Return df2 as Series for analytics calculation
        """
        #   Main DataFrame, cleaned by delete the surplus columns
        #   set the Student Code to Index
        df = self._clean_data(self.classDf)
        n = len(df) #   Length of original data
        df0 = df.copy()
        df0.set_index('Student Code', inplace=True)

        #   Set all missing answer to zero
        df0[df0 == ''] = 0

        #   Creat a copy of df0 as df1 then compare with answer
        answerKey = list('B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D'.split(','))
        df1 = df0.eq(answerKey)
        df1[df1 == True] = 4
        df1[df1 == False] = -1

        #   Find all postion of df0 with value 0
        #   Then move them to df1 with a copy of df2
        npZero = np.where(df0 == 0)
        zeroArray = np.array(npZero)
        x = [_ for _ in zeroArray[0, 0:]]
        y = [_ for _ in zeroArray[1, 0:]]
        zeroPostion = list(zip(x, y))

        #   Fill all zero point to df2
        for i in zeroPostion:
            df1.iloc[i] = 0

        #   If we move one column to another position before calculating
        #   It will show incorrect value
        df1['Exam Score'] = df1.sum(axis=1)

        #   creat ser3 as series to return
        ser = df1['Exam Score']
        return ser

    def _anylytics_result(self, dataFrame):
        return max(dataFrame), min(dataFrame), dataFrame.mean(), dataFrame.median()