# Trello
This is a small Python application I'm working on that interacts with the Trello API. It pulls and parses all the cards in my 'Monthly Food Expenses' board then displays my spending habits. It helps me visualize what months I'm spending more money. This project can be adapted to any board that has numerical data that needs to be computed and displayed.



##Requirements:
Add a file, in the root directory called `keys.txt` with your token and api_key in the following format:
token=alphanumeric
api_key=alphanumeric

Python 2.x
`pip install trollop`
`pip install seaborn`
`pip install matplotlib`


##Sample Trello Board with cards
![alt tag](https://raw.githubusercontent.com/211217613/trello-scraper/master/images/trello_screenshot.png)
##Sample Graph
![alt tag](https://raw.githubusercontent.com/211217613/trello-scraper/master/images/graph.png)