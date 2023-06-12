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


def plotbox(data):
    """
    This module is show the box plot of student grade area
    :param data: a series or dataframe
    :return: a box plot
    """
    plt.hist(data)
    # np.random.sceed(10)
    # fig, ax = plt.subplots()
    #
    # ax.hist(data, bins=20, linewidth=0.5, edgecolor="white")
    #
    # ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
    #        ylim=(0, 56), yticks=np.linspace(0, 56, 9))

    plt.show()
