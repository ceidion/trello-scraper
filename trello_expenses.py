#!/usr/bin/python
from trollop import TrelloConnection

import logging
from math import ceil
from time import strftime

import seaborn as sns
import matplotlib.pyplot as plt


# TODO: get exchange rate info from http://stackoverflow.com/questions/181990/programmatically-access-currency-exchange-rates?noredirect=1&lq=1
# TODO: Data Visualization, Error/exception handling
# TODO: clean up code, get feedback on reddit, maybe use args for spec params
# TODO: set up cron job to run every month


# idBoard': '577b17583e5d17ee55b20e44',
# idList': '577b17583e5d17ee55b20e45',
MONTHS = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug',
          'Sept', 'Oct', 'Nov', 'Dec']



class FrozenDict(object):
	def __init__(self, *args, **kwargs):
		# Hack to bypass `__setattr__`.
		self.__dict__['d'] = dict(*args, **kwargs)

	def __getattr__(self, key):
		return self.d[key]

	def __setattr__(self, key, val):
		raise TypeError('FrozenDict does not support setting attributes.')

	def __delattr__(self, key, val):
		raise TypeError('FrozenDict does not support deleting attributes.')

# TODO: use a json file for api key and token
def read_settings():
    with open('keys.txt', 'r') as keys:
        k = [line.split('=')[1].rstrip() for line in keys]
        token = k[0]
        api_key = k[1]
        return FrozenDict(
                          {'token':   k[0],
                           'api_key': k[1],
                           'board': 'BE89pW61'
                           }
                          )


def get_total_per_month(month, board_list):
    """Sums all the values in a month board.
    :param month: The month to calculate total for
    :param board_list: The entire Trello Board
    :return: The sum for the month not rounded
    """
    month = month.lower()
    return sum(float(crd.name.split('-')[1])
               for lst in board_list if month in lst.name.lower() for crd in lst.cards
            )

def get_yearly_average(totals):
    sum = 0.0
    count = 0
    for month in totals:
        if month != 0.0:
            count = count + 1
            sum += month
    year_average = sum / count
    print 'year ave {}'.format(str(year_average))
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

    # Establish connection
    conn = TrelloConnection(SETTINGS.api_key, SETTINGS.token)
    logging.info("Iterating through boards...")

    board = conn.get_board(SETTINGS.board)
    totals = [get_total_per_month(month, board.lists) for month in MONTHS]
    print totals
    average = get_yearly_average(totals)
    logging.info(totals)
    logging.debug('Board list: {}'.format(board.lists))
    plot(totals, average)

if __name__ == '__main__':
    SETTINGS = read_settings()

    # Set up basic logging
    logging.basicConfig(format='%(levelname)s %(message)s',
                        level=logging.INFO, filename='DEBUG.log',
                        filemode='w')
    main()
