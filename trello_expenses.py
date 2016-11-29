#!/usr/bin/python
from trollop import TrelloConnection

import logging
from math import ceil
from time import strftime

import seaborn as sns
import matplotlib.pyplot as plt

# Lots of issues with Python3. Lots of unicode, string errors, Just switched to
# py2. should try to use dicts for {name: cost} and to  practice using dicts

# TODO: Data Visualization, Error/exception handling
# TODO: clean up code, get feedback on reddit, maybe use args for spec params
# TODO: set up cron job to run every month
k = list()
with open('keys.txt', 'r') as keys:
    for line in keys:
        tmp = line.split('=')[1]
        tmp = tmp.rstrip()
        k.append(tmp)
token = k[0]
api_key = k[1]


# idBoard': '577b17583e5d17ee55b20e44',
# idList': '577b17583e5d17ee55b20e45',
# Set up basic logging
logging.basicConfig(format='%(levelname)s %(message)s',
                    level=logging.INFO, filename='DEBUG.log',
                    filemode='w')
# Establish connection
conn = TrelloConnection(api_key, token)
MONTHS = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug',
          'Sept', 'Oct', 'Nov', 'Dec']


logging.info("Iterating through boards...")


def get_total_per_month(month, board_list):
    costs = 0.0
    month = month.lower()
    for lst in board_list:
        if month in lst.name.lower():
            for crd in lst.cards:
                costs += float(crd.name.split('-')[1])
    return ceil(costs)


def first_of_the_month():
    day = strftime("%d")
    if '1' is day:
        pass


def get_yearly_average(totals):
    sum = 0.0
    count = 0
    for month in totals:
        if month != 0.0:
            count = count + 1
            sum += month
            # print month
    year_average = sum / count
    print 'year ave ' + str(year_average)
    return year_average


def plot(totals, average):
    sns.set(style='white', font_scale=1.5)
    plt.title('Monthly Food Expenses')
    plt.xlabel('Months')
    plt.ylabel('Pesos')
    sns.barplot(x=MONTHS, y=totals)
    plt.show()


def main():
    costs = list()
    names = list()

    board = conn.get_board('BE89pW61')
    totals = [get_total_per_month(month, board.lists) for month in MONTHS]
    print totals
    average = get_yearly_average(totals)
    logging.info(totals)
    logging.debug('Board list: {}'.format(board.lists))
    plot(totals, average)
if __name__ == '__main__':
    main()
