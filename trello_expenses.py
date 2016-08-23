#!/usr/bin/python
from trollop import TrelloConnection
import logging
# Lots of issues with Python3. Lots of unicode, string errors, Just switched to
# py2. should try to use dicts for {name: cost} and to  practice using dicts

# TODO: Data Visualization, Error/exception handling, appending to log for running total
# TODO: clean up code, get feedback on reddit, maybe use args for spec params
# TODO: set up cron job to run every month


api_key = '2819ec494f41829d45bdea15e3cf20e0'  # TRELLO_API_KEY
token = '0a46c305b380455a83176624e3e980fa8cfcba3b189a668558f3b03dc729a60e'
# idBoard': '577b17583e5d17ee55b20e44',
# idList': '577b17583e5d17ee55b20e45',
# Set up basic logging
logging.basicConfig(format='%(levelname)s %(message)s',
                    level=logging.INFO, filename='trello_expenses.log',
                    filemode='w')
# Establish connection
conn = TrelloConnection(api_key, token)
months = ['January', 'February', 'July', 'August',
          'September', 'October', 'November', 'December']
# Get expenses board via ID

logging.info("Iterating through boards...")

def main():
    total = 0.0
    costs = list()
    names = list()

    # get first index i.e the list im currently working on
    board = conn.get_board('BE89pW61')
    board_lists = board.lists
    logging.debug('Board list: {}'.format(board_lists))
    # Get all lists  names and ids in board
    for lists in board_lists:
        logging.debug('in month {}'.format(lists))
        total = 0.0
        for cards in lists.cards:
            name, cost = cards.name.split('-')
            costs.append(float(cost))
        total = sum(costs)
        print 'total is {} for month {}'.format(total, lists)
        logging.info( 'total is {} for month {}'.format(total, lists))
        del costs[:]

if __name__ == '__main__':
    main()
