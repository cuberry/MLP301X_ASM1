"""
This sub-module is used for:
- Display the first information of Assignment with display()
- Create the ask() function for any requirement applied
- Draw the histogram for vision
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def ask(prompt, retries=4):
    while True:
        check = input(prompt)
        if check in ('y', 'ye', 'yes', 'Y'):
            return True
        if check in ('n', 'no', 'nop', 'nope', 'N'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('Exit Program')


def display():
    print('')
    print('-' * 40)
    print('{:>20}'.format('Assigment #1'))
    print('{:>28}'.format('Class: MLP301x_1.2-A_VN'))
    print('{:>28}'.format('Originator: anhvtFX17079'))
    print('{:>25}'.format('Date: 09 Jun 2023'))
    print('{:>20}'.format('<This assignment is tested on Python3>'))
    print('-' * 40)


def barchart(data):
    """
    This module is show the box plot of student grade area
    :param data: a series or dataframe
    :return: a box plot
    """
    # Vẽ biểu đồ swarm
    x, y = list(data.index), data.values
    plt.figure(figsize=(16, 8))
    plt.bar(x, y)
    plt.plot(x, y, marker='o', markersize=10, linestyle='-.', linewidth=2)
    plt.xlabel('Student Code', fontsize=16)
    plt.ylabel('Exam Score', fontsize=16)
    plt.title('Histogram of Exam Score', fontsize=18)

    plt.show()


def boxplot(data):
    dims = list(data.values)
    plt.figure(figsize=(8, 8))
    plt.boxplot(dims)
    plt.xlabel('Student Code', fontsize=16)
    plt.ylabel('Score', fontsize=16)
    plt.title('Box PLot of Grade Score', fontsize=16)

    plt.show()
