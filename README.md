# Assignment 1 [![Build Status][ci-image]][ci] [![Code Climate][grade-image]][grade] 

This Assignment 1 is the first assigment program of MLP301X Machine Learning (FUNIX). The purpose of this assignment is to help student familiar with the basic function of Python data analysis: Pandas, Numpy and Matplotlib

### Project Name: Test Grade Calculator

## Assignment Requirement
-------------
Write a program to calculate test scores for many classes with thousands of students. The purpose of this program is to help reduce grading time. You will apply different functions in Python to write programs with the following tasks:

1. Open required external text files with exception-handling
2. Scan each line of test answers for valid data and provide the corresponding report
3. Scoring each test based on the rubrics provided and reported
4. Create a properly named result file

Program Structure
-------------
#### asm01_main: 

The main program to run the code, it collect sub function from asm01_file, asm01_display, asm01_data

#### asm01_file:
* Check the availability of file inside folder
* Load data from txt file then convert data to DataFrame
* Save the result of score/ grade to class*_grade.txt

#### asm01_display:

This sub-module is used for:
* Display the first information of Assignment with display()
* Create the ask() function for any requirement applied
* Draw the histogram for vision 


#### asm01_data:
class "Exam_Data" is created with descriptions below:
* The initiated instance of Exam_Data is one DataFrame which was collect from class[1..].txt
* Check_student_code(..) is used to verify the valid code of student
* Check_answer_quantity(..) is used to make sure the 25-answers
* Export the grade score
* Export the analytic values

README is the only file to provide guidelines of this Assignment.

How to run
--------
Run:

```ruby
Python asm01_main.py
```

Future Development
----------------
Class File can search/ find all location

Analytics Data can be viewed by Different Types of Plot

Useful Tools
------------
Pycharm for prorammming

Git repository for version control, integrated inside Pycharm



[community]: https://thoughtbot.com/community?utm_source=github
[hire]: https://thoughtbot.com/hire-us?utm_source=github
[ci-image]: https://github.com/thoughtbot/factory_bot/actions/workflows/build.yml/badge.svg?branch=main
[ci]: https://github.com/thoughtbot/factory_bot/actions?query=workflow%3ABuild+branch%3Amain
[grade-image]: https://codeclimate.com/github/thoughtbot/factory_bot/badges/gpa.svg
[grade]: https://codeclimate.com/github/thoughtbot/factory_bot
[version-image]: https://badge.fury.io/rb/factory_bot.svg
[version]: https://badge.fury.io/rb/factory_bot
[hound-badge-image]: https://img.shields.io/badge/Reviewed_by-Hound-8E64B0.svg
[hound]: https://houndci.com

