#!/usr/bin/python
from trollop import TrelloConnection
import matplotlib.pyplot as plt
import logging
from math import ceil
import plotting
from time import strftime

# Lots of issues with Python3. Lots of unicode, string errors, Just switched to
# py2. should try to use dicts for {name: cost} and to  practice using dicts

# TODO: Data Visualization, Error/exception handling, appending to log for running total
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
                    level=logging.INFO, filename='trello_expenses.log',
                    filemode='w')
# Establish connection
conn = TrelloConnection(api_key, token)
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']


logging.info("Iterating through boards...")

def get_total_per_month(month, board_list):
    costs = 0.0
    month = month.lower()
    for lst in board_list:
        if month in lst.name.lower():
            for crd in lst.cards:
                costs += float(crd.name.split('-')[1])
            # costs += float(lst.cards.name.split('-')[1])
    return ceil(costs)

def first_of_the_month():
    day = strftime("%d")
    if '1' is day:
        pass

def main():
    total = 0.0
    costs = list()
    names = list()

    board = conn.get_board('BE89pW61')
    totals = [ get_total_per_month(month, board.lists) for month in months]
    print totals
    logging.info(totals)
    logging.debug('Board list: {}'.format(board.lists))

if __name__ == '__main__':
    main()
