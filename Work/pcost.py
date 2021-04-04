# pcost.py
#
# Exercise 1.27

import csv
import sys


'''
Returns total cost of portfolio using csv module
'''
def portfolio_cost_csv(file_name):
    total_cost = 0
    
    with open(file_name, 'rt') as data_file:
        rows = csv.reader(data_file)
        
        headers = next(rows)
        
        for rowNo, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                total_cost += int(record['shares']) * float(record['price'])
            except ValueError:
                print(f'WARNING! Incorrect data: {row} at row number {rowNo}')
    
    return total_cost


'''
Returns total cost of portfolio
'''
def portfolio_cost(file_name):
    total_cost = 0

    with open(file_name, 'rt') as data_file:
        headers = next(data_file)
        
        for rowNo, row in enumerate(data_file):
            row_split = row.split(',')
            record = dict(zip(headers, row_split))
            try:
                record['price'] = record['price'].strip()
                
                total_cost += int(record['shares']) * float(record['price'])
            except ValueError:
                print(f'WARNING! Incorrect data: {row} at row number {rowNo}')
    
    return total_cost


is_csv_true = True

if len(sys.argv) == 3:
    file_name = sys.argv[1]
    if sys.argv[2] == 'n':
        is_csv_true = False
elif len(sys.argv) == 2:
    file_name = sys.argv[1]
else:
    file_name = 'Data/portfolio.csv'

if is_csv_true:
    print('Function called: portfolio_cost_csv')
    cost = portfolio_cost_csv(file_name)
else:
    print('Function called: portfolio_cost')
    cost = portfolio_cost(file_name)

print(f'Total cost {cost:0.2f}.')