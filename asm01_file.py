"""
Class "File" contains:
    - Check the availability of file inside folder
    - Load data from txt file then convert data to DataFrame
    - Save the result of score/ grade to class*_grade.txt
"""
import os
import pandas as pd
from asm01_display import *

fileName = input('Please enter the class name: ')   #public the file name

class File:
    def __init__(self, currentDir = None):
        if not currentDir:
            currentDir = os.getcwd() + '\\Data Input\\'
        else:
            self.currentDir = currentDir

    def load_data(self):
        """
        This module is to check the availability of file
        In the requirement of assigment, the location of file is in the same folder as default
        :return: The 2-dim matrix (List) of class data
        Development: searching the file/ try another location/ enter few times for correct filename
        """
        print('!Note:\n'
              'The assigment needs to load the dataset from file {}\n'
              'If you do not enter the path to access the file,\n'
              'the data file shall be loaded in this current directory as default'.format(fileName))

        loadCheck = ask('\nThe file is in the same directory with core python file? Y/n: ')

        if not loadCheck:
            print('Please copy it to the same location then try again!')
            quit()
        else:
            try:
                f = open(os.getcwd() +'\\Data Input\\' + fileName + '.txt', 'r')
                print('File is found! Processing to load the data ...')
                rawData = [[i for i in j.split(',')] for j in f.read().split()]
                classDf = pd.DataFrame(rawData).rename(columns={0: 'Student Code'})
                f.close()
                print('Load data successful! Proceed the next steps ...')
                return classDf
            except IOError:
                #   If the file is not found, return nothing
                print('File is not found!')
                quit()

    def save_data(self, data, fileName):
        """

        :param data: DataFrame or Series of result
        :param fileName: file name to save the analysis result
        :return: the fileName with "class*_grade.txt"
        """
        path = os.getcwd() + '\\Expected Output\\'
        data.to_csv(path + fileName + '_grade.txt', sep=',', header=False, index=True)

    def load_full_result_data(self):
        #   Data must be available at the same directory
        try:
            with os.scandir() as it:
                for entry in it:
                    if not entry.name.startswith('class') and entry.is_file():
                        print('No data file is found inside folder!')
                    else:
                        #   Data are loaded from folder
                        for file in os.getcwd():
                            if file.startswith('class') and file.endswith('txt'):
                                userData = pd.read(file)
            return userData
        except FileNotFoundError:
            #   If the file is not found, try to re-search in 4 times
            ask('Path is not found! Do you want to try another? Y/n: ')

    def load_result(self, fileName):
        """
        This module is used to load the result of data to view
        :param fileName:
        :return: the display of result in matplot lib or table dataframe
        """
        pass