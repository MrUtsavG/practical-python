# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    months += 1
    
    if extra_payment_start_month <= months <= extra_payment_end_month:
        if principal * (1+rate/12) < (payment + extra_payment):
            final_payment = principal * (1+rate/12)
            principal = principal * (1+rate/12) - final_payment
            total_paid += final_payment
        else:
            principal = principal * (1+rate/12) - (payment + extra_payment)
            total_paid = total_paid + payment + extra_payment
    else:
        if principal * (1+rate/12) < payment:
            final_payment = principal * (1+rate/12)
            principal = principal * (1+rate/12) - final_payment
            total_paid += final_payment
        else:
            principal = principal * (1+rate/12) - payment
            total_paid = total_paid + payment
    
    print(f'{months} Total paid: {total_paid:0.2f} Principal Amount: {principal:0.2f}')
