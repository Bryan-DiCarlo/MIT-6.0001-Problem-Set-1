# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:16:41 2020

@author: bryan
"""

# In part A we assumed salary was constant.  Use the code produced from part A
# But now figure in a semi-annual raise
#1.Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage) 
#2.After the 6 th month, increase your salary by that percentage. Do the same after the 12th th month, the 18 month, and so on.
# Otherwise use the assumptions from below for part A


#In Part A, we are going to determine how long it will take you to save enough money to make the down payment given the following 
#assumptions: 
#    1.Call the cost of your dream home total_cost . 
#    2.Call the portion of the cost needed for a down payment portion_down_payment . For simplicity, 
#    assume that portion_down_payment = 0.25 (25%). 
#    3.Call the amount that you have saved thus far current_savings . You start with a current savings of $0. 
#    4.Assume that you invest your current savings wisely, with an annual return of r 
#    (in other words, at the end of each month, you receive an additional current_savings*r/12 funds to put into your savings – 
#     the 12 is because r is an annual rate). Assume that your investments earn a return of r = 0.04 (4%). 
#    5.Assume your annual salary is annual_salary . 
#    6.Assume you are going to dedicate a certain amount of your salary each month to saving for the down payment. Call that 
#    portion_saved . This variable should be in decimal form (i.e. 0.1 for 10%). 
#    7.At the end of each month, your savings will be increased by the return on your investment, plus a percentage of your 
#    monthly salary (annual salary / 12).
#Write a program to calculate how many months it will take you to save up enough money for a down payment.


annual_salary = float(input('Enter you annual salary:>>> '))
portion_saved = float(input('Enter precentage of salary to save:>>> '))
total_cost = float(input('Enter the cost of your dream home:>>> '))
semi_annual_raise = float(input('Enter semi annual raise, as a decimal:>>> '))

current_savings = 0
monthly_salary = annual_salary/12
months = 0
portion_down_payment = total_cost * 0.25
r = 0.04


while current_savings < portion_down_payment:
    current_savings += (monthly_salary * portion_saved) + (current_savings *(r/12))
    months += 1
    if months % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise
        
print(f'Number of months = {months}')
