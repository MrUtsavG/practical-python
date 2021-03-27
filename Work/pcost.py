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
        
        for row in rows:
            try:
                total_cost += int(row[1]) * float(row[2])
            except ValueError:
                print('WARNING! Incorrect data at', row)
    
    return total_cost


'''
Returns total cost of portfolio
'''
def portfolio_cost(file_name):
    total_cost = 0

    with open(file_name, 'rt') as data_file:
        headers = next(data_file)
        
        for line in data_file:
            line_split = line.split(',')
            try:
                line_split[2] = line_split[2].strip()
                
                total_cost += int(line_split[1]) * float(line_split[2])
            except ValueError:
                print('WARNING! Incorrect data at', line)
    
    return total_cost


is_csv_true = False

if len(sys.argv) == 3:
    file_name = sys.argv[1]
    if sys.argv[2] == 'y':
        is_csv_true = True
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