"""
The problems:
    1. The answer list is failed if the quantity of answer is < 25 or > 25
    2. Anwer quantity must be equal 25 and without 'N/A' - missing answer
    3. Student Code:
        a. Start with N
        b. Format with 'N' and 8-digits
The solution must be check all condition and return the problem
"""
from asm01_data import *
from asm01_display import *
from asm01_file import *

if __name__ == '__main__':
    display()

    #   Setup an object to call the file
    #   Then load data to dataframe
    f = File()
    myDataFrame = f.load_data()
    print('Data loaded from file: ...')
    print(myDataFrame)

    #   Print result of analysis
    classData = ClassGrade(myDataFrame)
    print('=.='*4, 'ANALYSING', '=.='*4)
    df1 = classData._check_student_code()
    df2 = classData._check_answer_quantity()

    if not df1.empty:
        print('Invalid number of student code: N# is invalid')
        print(df1)
    if not df2.empty:
        print('Invalid quantity of answer: not 25 values')
        print(df2)
    else:
        print('No error found! ...')

    #   Data Analytics
    seriesData = classData._grade_student()
    print('=.='*4, 'STUDEN SCORE TABLE', '=.='*4)
    print(seriesData)

    #   Print Report
    totalLineCount = len(myDataFrame)
    invalidLineCount1 = len(df1) if not df1.empty else 0
    invalidLineCount2 = len(df2) if not df2.empty else 0
    invalidLineCount = invalidLineCount1 + invalidLineCount2
    validLineCount = totalLineCount - invalidLineCount
    print('=.='*4, 'REPORT', '=.='*4)
    print('Total {} recorded lines of data.'.format(totalLineCount))
    print('Total {} invalid lines of data.'.format(invalidLineCount))
    print('Total {} valid lines of data.'.format(validLineCount))
    print('Mean (avarage score): ', round(seriesData.mean(), 2))
    print('Highest Score: ', round(seriesData.max(),2))
    print('Lowest Score:', round(seriesData.min(),2))
    print('Range of Score:', round(seriesData.quantile(),2))

    f.save_data(seriesData, fileName)

    #   barchart(seriesData)
    #   Change bar chart to box plot
    boxplot(seriesData)





