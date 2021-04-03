# report.py
#
# Exercise 2.4

import csv
from pprint import pprint

portfolio = []
prices = {}
report = []
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


'''
Returns list of tuples containing rows of report
'''
def make_report(port, curr_prices):
    report_list = []
    
    header = ('Name', 'Shares', 'Current Price', 'Change')
    report_list.append(header)
    
    delim = f"{'-'*15}"
    new_line = (delim, delim, delim, delim)
    report_list.append(new_line)
    
    for holding in port:
        curr_price = curr_prices[holding['name']]
        price_change = curr_price - holding['price']
        
        row = (holding['name'], holding['shares'], curr_price, price_change)
        report_list.append(row)

    return report_list


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

for index, row in enumerate(report):
    if index == 0 or index == 1:
        print(f"{row[0]:>15s} {row[1]:>15s} {row[2]:>15s} {row[3]:>15s}")
    else:
        dollar_price = f"${row[2]:0.2f}"
        print(f"{row[0]:>15s} {row[1]:>15d} {dollar_price:>15s} {row[3]:>15.2f}")

for holding in portfolio:
    price_diff = prices[holding['name']] - holding['price']
    gain_loss += holding['shares'] * price_diff

print('\nGain/Loss in portfolio -', gain_loss)