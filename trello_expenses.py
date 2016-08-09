#!/usr/bin/python
from trollop import TrelloConnection
import logging 
import argparse
# Lots of issues with Python3. Lots of unicode, string errors, Just switched to 
# py2. should try to use dicts for {name: cost} and to  practice using dicts 

# TODO: Data Visualization, Error/exception handling, appending to log for running total
# TODO: clean up code, get feedback on reddit, maybe use args for spec params
# TODO: set up cron job to run every month
api_key = '2819ec494f41829d45bdea15e3cf20e0' # TRELLO_API_KEY
token = '0a46c305b380455a83176624e3e980fa8cfcba3b189a668558f3b03dc729a60e'
# idBoard': '577b17583e5d17ee55b20e44',
# idList': '577b17583e5d17ee55b20e45',
# Set up basic logging
logging.basicConfig(format='%(message)s',
    level=logging.INFO, filename='trello_expenses.log', filemode='w')

# Establish connection
conn = TrelloConnection(api_key, token)
months = ['January', 'February', 'July', 'August', \
          'September','October','November', 'December']
# Get expenses board via ID

logging.info("Iterating through boards...")

# for board in conn.me.boards:
#     # logging.info("id: {}".format(each._id))
#     # print u"board name: {0}, board id {1}" . format( board.name, board._id )  
#     logging.info (u"board name: {0}, board id {1}".\
#                     format( board.name, board._id ))  

# for each_card in conn.me.boards[2].cards:
#     print u"{0},{1},{2}".format(each_card._id, each_card.url,each_card.desc)  


def main():
    total = 0.0
    names = list()
    costs = list()

    # Set up connection and get reference to board
    board = conn.get_board('BE89pW61')
    board_lists = board.lists
    logging.info('board_lists: {}'.format( board_lists) )

    # Iterate through lists adding up all costs and logging them
    for lists in board_lists:
        total = 0.0
        logging.info('In {} month'.format(lists) )
        for cards in lists.cards:
            name, cost =  cards.name.split('-')
            names.append( name )
            costs.append( float(cost) )
            logging.info(name)
        total = sum (costs)
        logging.info('Total for {} is {}'.format( lists, total) )
        del costs[:]


if __name__=='__main__':
    main()