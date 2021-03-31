# report.py
#
# Exercise 2.4

import csv
from pprint import pprint

portfolio = []
prices = {}
gain_loss = 0


'''
Returns portfolio list from file name
'''
def read_portfolio(file_name):
    read_port = []
    with open(file_name, 'rt') as open_file:
        rows = csv.reader(open_file)
        headers = next(rows)
        
        for row in rows:
            holding = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
                }
            
            read_port.append(holding)
    
    return read_port


'''
Returns prices of stocks from file_name
'''
def read_prices(file_name):
    read_pr = {}
    with open(file_name, 'rt') as open_file:
        rows = csv.reader(open_file)
        
        for row in rows:
            if row:
                read_pr[row[0]] = float(row[1])
    
    return read_pr


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')


for holding in portfolio:
    price_diff = prices[holding['name']] - holding['price']
    gain_loss += holding['shares'] * price_diff

print('Gain/Loss in portfolio -', gain_loss)